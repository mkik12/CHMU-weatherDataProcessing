# This is a part of "ČHMÚ/CHMI – Meteorological Data Processing" a QGIS plugin
# that processes meteorological data published by CHMI.  
# Copyright (C) 2025 by Mikuláš Kadečka - mikulas.kad@seznam.cz  

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from functions import *

def mainFunction(parameters: dict):

    ## Storing parameters from dictionary to variables

    dataPath = parameters["dataPath"]
    outputPath = parameters["outputPath"]
    outputName = parameters["outputName"]
    intersectArea = parameters["intersectArea"]
    startDate = parameters["startDate"]
    endDate = parameters["endDate"]
    interpolationMethod = parameters["interpolationMethod"]
    cellSize = parameters["cellSize"]
    crs = parameters["epsg"]
    tempDir = parameters["tempDir"]
    power = parameters["power"]
    category = parameters["category"]
    pointOutput = parameters["pointOutput"]

    ## Loading and reprojecting the station point layer
    layer = QgsVectorLayer(os.path.join(dataPath, "stations.gpkg"), "stations", "ogr")
    projectedLayer = processing.run("native:reprojectlayer", {'INPUT': layer,
                                                             'TARGET_CRS': crs,
                                                             'OUTPUT': 'TEMPORARY_OUTPUT'})
    stationsLayer = projectedLayer["OUTPUT"]

    ## Resizing the extent layer (if necessary), reprojecting it, and creating a bounding geometry
    ## for consistent selection of stations
    try:
        intersectArea = user.resizeExtent(intersectArea)
        projectedArea = processing.run("native:reprojectlayer", {'INPUT': intersectArea,
                                                                        'TARGET_CRS': crs,
                                                                        'OUTPUT': 'TEMPORARY_OUTPUT'})
        
        intersectAreaAsEnvelope = processing.run("qgis:minimumboundinggeometry", {
                                                    'INPUT': projectedArea["OUTPUT"],
                                                    'FIELD': '',
                                                    'TYPE': 0,
                                                    'OUTPUT': 'TEMPORARY_OUTPUT'})
    except:
        return 4
    
    ## Selecting the stations of interest
    stationsLayerSelected = processing.run("native:selectbylocation", {
                                            'INPUT': stationsLayer,
                                            'PREDICATE': [0],
                                            'INTERSECT': intersectAreaAsEnvelope["OUTPUT"],
                                            'METHOD': 0})

    ## Creating date intervals for different iterations of raster interpolation and calculating 
    ## the corresponding values
    intersectAreaExtent = intersectAreaAsEnvelope["OUTPUT"].extent()
    extentCoordinates = info.getExtentAsSingleCoordinates(intersectAreaExtent)

    if stationsLayer.selectedFeatureCount() == 0:
        return 1

    dateCondition = (startDate, endDate)
    metadata = info.getFeaturesMetadata(stationsLayer, dateCondition)

    IDs = metadata[0]
    dates = metadata[1]

    info.printDates(dates)

    if not dates:
        return 2
    
    dataBox = utils.prepareDataBox(IDs)

    data = essentials.meanValuePerDate(IDs, dates, dataBox, dataPath)

    ## Weights will later be used to calculate the weighted average raster for the final output of the plugin
    weights = utils.getWeights(dates)
    weightDivisor = 0

    interpolatedRasters = []
    layersToLoad = []

    ## Creating a separate station point layer for each date interval, interpolating them, and creating
    ## rasters stored as a numpy array (a better approach than using the buggy Raster Calculator)
    for i in range(len(dates)):

        memoryLayer = QgsVectorLayer(f"Point?crs={crs.authid()}", "layer", "memory")
        provider = memoryLayer.dataProvider()
        
        providerInfo = essentials.stationsPerDateAsPoints(data, i, stationsLayer)
        
        provider.addAttributes(providerInfo[0])
        memoryLayer.updateFields()
        
        provider.addFeatures(providerInfo[1])

        tempPath = utils.getTempPath(".gpkg", tempDir)
        
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = "GPKG"
        options.fileEncoding = "UTF-8"
        options.crs = memoryLayer.crs()
        QgsVectorFileWriter.writeAsVectorFormatV3(memoryLayer, tempPath, QgsCoordinateTransformContext(), options)
        layersToLoad.append(tempPath)

        arrayRaster = raster.rasterInterpolationAsArr(tempPath, intersectAreaExtent, extentCoordinates, cellSize, interpolationMethod, power)

        if not np.any(arrayRaster.astype(int) == -9999):
            weightedArrRaster = arrayRaster * weights[0]
            interpolatedRasters.append(weightedArrRaster)
            weightDivisor += weights[0]

        weights.pop(0)

    ## Creating the weighted average raster from the interpolated data
    if len(interpolatedRasters) == 0:
        return 2
    else:
        finalArrRaster = raster.createFinalArrRaster(interpolatedRasters, weightDivisor)

    ## Saving the numpy raster in ASCII format is the easiest way to convert it into a GIS-compatible format
    tempPath = utils.getTempPath(".asc", tempDir)

    raster.createFinalTXTRaster(tempPath, finalArrRaster, extentCoordinates, cellSize)

    ## Saving the raster in the format specified by the user
    if outputPath is None:
        layer = processing.run("gdal:translate", {'INPUT':tempPath, 'OUTPUT' : 'TEMPORARY_OUTPUT'})
        outputLayer = QgsRasterLayer(layer["OUTPUT"], outputName)
        outputLayer.setCrs(crs)
    else:
        processing.run("gdal:translate", {'INPUT':tempPath, 'OUTPUT' : outputPath})
        processing.run("gdal:assignprojection", {'INPUT':outputPath,'CRS': crs})
        outputLayer = QgsRasterLayer(outputPath, outputName)

    ## Loading the final raster into the QGIS project and optionally loading the point layers
    ## used for interpolation
    QgsProject.instance().addMapLayer(outputLayer)
    try:
        if pointOutput is False:
            info.loadInterpolatedLayers(layersToLoad, dates, category)
    except:
        return 3
    
    ## Removing the temporary files created by this program
    utils.removeTempFiles(tempDir)
    return 0

# This is a part of "ČHMÚ - Data o počasí," a QGIS plugin that processes meteorological data published by CHMI.  
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

    layer = QgsVectorLayer(os.path.join(dataPath, "stations.gpkg"), "stations", "ogr")
    projectedLayer = processing.run("native:reprojectlayer", {'INPUT': layer,
                                                             'TARGET_CRS': crs,
                                                             'OUTPUT': 'TEMPORARY_OUTPUT'})
    stationsLayer = projectedLayer["OUTPUT"]
    
    projectedArea = processing.run("native:reprojectlayer", {'INPUT': intersectArea,
                                                                       'TARGET_CRS': crs,
                                                                       'OUTPUT': 'TEMPORARY_OUTPUT'})
        
    intersectAreaAsEnvelope = processing.run("qgis:minimumboundinggeometry", {
                                                'INPUT': projectedArea["OUTPUT"],
                                                'FIELD': '',
                                                'TYPE': 0,
                                                'OUTPUT': 'TEMPORARY_OUTPUT'})

    stationsLayerSelected = processing.run("native:selectbylocation", {
                                            'INPUT': stationsLayer,
                                            'PREDICATE': [0],
                                            'INTERSECT': intersectAreaAsEnvelope["OUTPUT"],
                                            'METHOD': 0})

    ## 3.2 Variable preparation for further processing
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
    
    weights = utils.getWeights(dates)
    weightDivisor = 0

    interpolatedRasters = []
    layersToLoad = []

    ## 3.3 Cycle that creates a list of weighted NumPy arrays generated from raster interpolation
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
        # options.ct = QgsCoordinateTransformContext()
        options.crs = memoryLayer.crs()
        # tempPath = f"C:\\Users\\mikul\\Desktop\\Bakalářská práce\\TEMP\\{i}.gpkg"
        QgsVectorFileWriter.writeAsVectorFormatV3(memoryLayer, tempPath, QgsCoordinateTransformContext(), options)
        layersToLoad.append(tempPath)

        arrayRaster = raster.rasterInterpolationAsArr(tempPath, intersectAreaExtent, extentCoordinates, cellSize, interpolationMethod, power)

        if not np.any(arrayRaster.astype(int) == -9999):
            weightedArrRaster = arrayRaster * weights[0]
            interpolatedRasters.append(weightedArrRaster)
            weightDivisor += weights[0]

        weights.pop(0)

    ## 3.4 Creating the weighted average raster
    if len(interpolatedRasters) == 0:
        return 2
    else:
        finalArrRaster = raster.createFinalArrRaster(interpolatedRasters, weightDivisor) #fungovalo by to i bez podmínky

    ## 3.5 Saving the final raster in ASCII raster format (GIS format) 
    tempPath = utils.getTempPath(".asc", tempDir)

    raster.createFinalTXTRaster(tempPath, finalArrRaster, extentCoordinates, cellSize)

    if outputPath is None:
        layer = processing.run("gdal:translate", {'INPUT':tempPath, 'OUTPUT' : 'TEMPORARY_OUTPUT'})
        outputLayer = QgsRasterLayer(layer["OUTPUT"], outputName)
        outputLayer.setCrs(crs)
    else:
        processing.run("gdal:translate", {'INPUT':tempPath, 'OUTPUT' : outputPath})
        processing.run("gdal:assignprojection", {'INPUT':outputPath,'CRS': crs})
        outputLayer = QgsRasterLayer(outputPath, outputName)

    ## 3.6 Loading the program output into the current QGIS project
    QgsProject.instance().addMapLayer(outputLayer)
    try:
        if pointOutput is False:
            info.loadInterpolatedLayers(layersToLoad, dates, category)
    except:
        return 3
    utils.removeTempFiles(tempDir)
    return 0
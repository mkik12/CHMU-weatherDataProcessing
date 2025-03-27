import numpy as np
from osgeo import gdal
import processing
import time

def rasterInterpolationAsArr(path: str, extent, extentCoordinates, cellSize: float, method: str, power: int) -> np.array:

    '''
    Creates a raster from a vector point layer using the specified interpolation method.  
    The raster is then converted into a NumPy array for generating the weighted average raster.
    '''

    xMin, yMin, xMax, yMax = extentCoordinates

    width = abs(xMax - xMin)
    heigth = abs(yMax - yMin)

    pixelXCount = width / cellSize
    pixelYCount = heigth / cellSize

    if method == "IDW":
        raster = processing.run("qgis:idwinterpolation", {
            'INTERPOLATION_DATA':f"{path}::~::0::~::1::~::0",
            'DISTANCE_COEFFICIENT': power,
            'EXTENT': extent,
            'PIXEL_SIZE': cellSize,
            'OUTPUT': "TEMPORARY_OUTPUT"})
        
    elif method == "Nearest Neighbour":

        raster = processing.run("gdal:gridnearestneighbor", {
            'INPUT':path,
            'Z_FIELD':'value',
            'RADIUS_1':0,
            'RADIUS_2':0,
            'ANGLE':0,
            'NODATA':0,
            'OPTIONS':'',
            'EXTRA':f'-txe {xMin} {xMax} -tye {yMin} {yMax} -outsize {pixelXCount} {pixelYCount}',
            'DATA_TYPE':5,
            'OUTPUT':'TEMPORARY_OUTPUT'})

    openedRaster = gdal.Open(raster["OUTPUT"])

    rasterAsArr = openedRaster.GetRasterBand(1).ReadAsArray()
    
    return rasterAsArr
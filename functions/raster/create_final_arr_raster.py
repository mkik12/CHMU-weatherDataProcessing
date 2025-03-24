import numpy as np

def createFinalArrRaster(rasters: list, divisor: int) -> np.array:
    '''
    Computes a weighted average raster from a list of NumPy arrays 
    and returns the resulting raster as a NumPy array.
    '''

    newRaster = rasters[0]
    #count = len(rasters)
    i = 0
    for raster in rasters[1:]:
        newRaster = newRaster + np.array(raster)
        i += 1
        #print(i, np.array(raster))
        
    return newRaster/divisor
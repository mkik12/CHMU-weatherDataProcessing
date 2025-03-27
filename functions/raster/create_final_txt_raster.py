def createFinalTXTRaster(path, arrRaster, extent: tuple, cellSize: float) -> None:
    '''
    Stores the final NumPy array raster in ASCII format for GIS compatibility.
    '''

    with open(path, "w") as file:
        file.write(f"NCOLS {arrRaster.shape[1]}\n")
        file.write(f"NROWS {arrRaster.shape[0]}\n")
        file.write(f"XLLCORNER {extent[0]}\n")
        file.write(f"YLLCORNER {extent[1]}\n")
        file.write(f"CELLSIZE {cellSize}\n")
        file.write(f"NODATA_VALUE -9999")
        file.write("\n")
        for line in arrRaster:
            file.write(" ".join(line.astype(str).tolist()))
            file.write("\n")
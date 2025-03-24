def getExtentAsSingleCoordinates(extent) -> tuple:
    '''
    Accepts a QgsRectangle as input and returns a tuple containing 
    decimal numbers representing the X and Y minimum and maximum coordinates.
    '''

    xMin = extent.xMinimum()
    xMax = extent.xMaximum()
    yMin = extent.yMinimum()
    yMax = extent.yMaximum()

    return (xMin, yMin, xMax, yMax)
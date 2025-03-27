def getExtentAsSingleCoordinates(extent) -> tuple:
    '''
    Accepts a QgsRectangle as input and returns a tuple of decimal numbers 
    representing the minimum and maximum X and Y coordinates.
    '''

    xMin = extent.xMinimum()
    xMax = extent.xMaximum()
    yMin = extent.yMinimum()
    yMax = extent.yMaximum()

    return (xMin, yMin, xMax, yMax)
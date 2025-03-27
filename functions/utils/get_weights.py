def getWeights(dates: list) -> list:
    '''
    Computes a list of integers based on the day count of each date interval.  
    These weights are used to calculate the weighted average raster.
    '''
    
    weights = []
    for date in dates:

        startDate = date[0]
        endDate = date[1]

        days = (startDate.daysTo(endDate))
        weights.append(days)

    return weights
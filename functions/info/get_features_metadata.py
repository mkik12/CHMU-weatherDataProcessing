from copy import deepcopy
from datetime import datetime
from PyQt5.QtCore import QDate

def cutDates(dates: list, conditionDate: datetime, start = True) -> list:
    newDates = []

    if start is True:
        dates = dates[::-1]

        for date in dates:
            if date > conditionDate:
                newDates.append(date)
                continue
            if date == conditionDate:
                newDates.append(conditionDate)
                break
            if date < conditionDate:
                newDates.append(conditionDate)
                break

        return newDates[::-1]
    
    if start is False:
        for date in dates:
            if date < conditionDate:
                newDates.append(date)
                continue
            if date == conditionDate:
                newDates.append(conditionDate)
                break
            if date > conditionDate:
                newDates.append(conditionDate)
                break

        return newDates
    
def getDates(features) -> list:
    allDates = []

    for feature in features:

        startDate = feature[4]
        allDates.append(startDate)
    
        endDate = feature[5]
        allDates.append(endDate)

    return allDates

def getUniqueDates(dates) -> list:
    uniqueDates = list(set(dates))

    return uniqueDates


def getFeaturesMetadata(layer, dateCondition: tuple) -> tuple:
    '''
    Returns a tuple of lists containing:\n 
    * date intervals (based on the user's date condition and the station's measurement 
    activity - date intervals are stored in chronological order)\n
    * IDs (of selected station features)
    '''

    selectedStations = [feature for feature in layer.getSelectedFeatures()]

    allDates = getDates(selectedStations)
    IDs = getIDs(selectedStations)

    pairedDates = pairDates(allDates)
    # print(pairedDates)

    if isDateConditionValiable(dateCondition, pairedDates) is True:
        uniqueDates = getUniqueDates(allDates)
        sortedDates = sortDates(uniqueDates)
        
        if dateCondition[0] > sortedDates[0]:
            if isinstance(dateCondition[0], datetime):
                startDate = QDate(dateCondition[0].year, dateCondition[0].month, dateCondition[0].day)
            else: 
                startDate = dateCondition[0]
        else:
            startDate = sortedDates[0]
        if dateCondition[-1] < sortedDates[-1]:
            if isinstance(dateCondition[-1], datetime):
                endDate = QDate(dateCondition[-1].year, dateCondition[-1].month, dateCondition[-1].day)
            else: 
                endDate = dateCondition[-1]
        else:
            endDate = sortedDates[-1]

        sortedDates = cutDates(sortedDates, startDate)
        sortedDates = cutDates(sortedDates, endDate, start = False)
    else:
        sortedDates = []

    return (IDs, datesCombinations(sortedDates))

def getIDs(features) -> list:
    IDs = []
    
    for feature in features:
        IDs.append(feature[1])

    return IDs

def isDateConditionValiable(condition, pairedDates) -> bool:
    
    for date in pairedDates:
        # if date[-1] >= condition[0] >= date[0] or date[0] <= condition[-1] <= date[-1]:
        if date[-1] > condition[0] >= date[0] or date[0] < condition[-1] <= date[-1]:
            return True
        if condition[-1] > date[0] > condition[0] and condition[0] < date[-1] < condition[-1]:
            return True

    return False

def pairDates(dates) -> list:
    pairedDates = []

    dates01 = deepcopy(dates)

    while dates01:
        pairedDates.append((dates01[0], dates01[1]))
        dates01.pop(0)
        dates01.pop(0)
    
    return pairedDates

def sortDates(dates) -> list:
    sortedDates = []

    while dates:
        newDate = dates[0]
        for date in dates:
            if date < newDate:
                newDate = date
        sortedDates.append(newDate)
        dates.remove(newDate)

    return sortedDates

def datesCombinations(dates) -> list:
    pairedDates = []

    for i in range(len(dates)):
        if i + 1 <= len(dates) - 1:
            pairedDates.append((dates[i], dates[i + 1]))
    
    return pairedDates
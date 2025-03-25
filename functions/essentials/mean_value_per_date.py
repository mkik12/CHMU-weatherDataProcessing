from copy import deepcopy
from datetime import datetime
from PyQt5.QtCore import QDate
import os

from qgis.core import(
    QgsVectorLayer
)

def meanValuePerDate(IDs, dates, data, dataPath):
    '''
    Computes the mean value for each selected station and its date intervals.
    These values are stored in the lists of the "dataBox" according to their feature IDs
    as decimal numbers or None.\n
    (None is used if there is no measurment activity for the selected date interval)
    '''
    for ID in IDs:

        dates01 = deepcopy(dates)
        table = QgsVectorLayer(os.path.join(dataPath, str(ID) + ".gpkg"), str(ID), "ogr")
    
        if table.featureCount() == 0:
            del data[ID]
            continue
            
        newValue = None
        count = 0
            
        for feature in table.getFeatures():
            if not dates01:
                break
                
            attributes = feature.attributes()
            
            year = attributes[1]
            month = attributes[2]
            day = attributes[3]
            value = attributes[4]
            
            featureDate = QDate(year, month, day)

            while dates01 and dates01[0][1] < featureDate:

                dates01.pop(0)
                data[ID].append(None)

            if not dates01:
                break
            
            if dates01[0][0] <= featureDate < dates01[0][1]:
                if newValue is None:
                    newValue = value
                    count = 1
                else:
                    newValue += value
                    count += 1
                continue
            
            if featureDate < dates01[0][0]:
                continue

            if featureDate == dates01[0][1]:
                if newValue is not None:
                    newValue = (newValue + value) / (count + 1)
                    newValue = round(newValue, 3)
                    data[ID].append(newValue)

                else:
                    data[ID].append(None)

                dates01.pop(0)

                newValue = None
                count = 0

                continue

            # if dates01[0][1] < featureDate:
            #     dates01.pop(0)

            #     if newValue is None:
            #         newValue = value
            #         count = 1
            #     else:
            #         newValue += value
            #         count += 1

            #     data[ID].append(None)

        if dates01 and newValue is not None:
            newValue = newValue/count
            newValue = round(newValue, 3)
            data[ID].append(newValue)
            
            dates01.pop(0)
                    
        if dates01:
            for _ in dates01:
                data[ID].append(None)
                
    return data
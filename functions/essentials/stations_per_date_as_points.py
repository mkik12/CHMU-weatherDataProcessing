from PyQt5.QtCore import QVariant

from qgis.core import(
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsFeature,
)

def stationsPerDateAsPoints(data: dict, i: int, points: QgsVectorLayer):
    '''
    Creates point features for vector layer with a "value" attribute representing
    the mean value of the selected stations based on their date interval.\n
    This function works with the items stored in the "dataBox".
    '''

    newFeatures = []
    fields = QgsFields()
    fields.append(QgsField('value', QVariant.Double))
    
    for feature in points.getSelectedFeatures():

        if feature["fileID"] not in data:
            continue
        # if len(data[feature["ID"]]) != 0 and data[feature["ID"]][i] != None:
        if data[feature["fileID"]][i] != None:
        
            new_value = data[feature["fileID"]][i]
        
            newFeature = QgsFeature(fields)
            newFeature.setAttributes([new_value])
            newFeature.setGeometry(feature.geometry())
        
            newFeatures.append(newFeature)
    return (fields, newFeatures)
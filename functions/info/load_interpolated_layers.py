import processing
from qgis.core import (
    QgsProject,
    QgsLayerTreeGroup,
    QgsVectorLayer
)

def loadInterpolatedLayers(inputLayers, dates, category):

    root = QgsProject.instance().layerTreeRoot()
    group = root.addGroup(f"{category} - bodová pole")

    for date, layer in zip(dates, inputLayers):

        vectorLayer = QgsVectorLayer(layer, "layer", "ogr")

        result = processing.run("native:package", {
            'LAYERS':[vectorLayer],
            'OUTPUT':'TEMPORARY_OUTPUT',
            'OVERWRITE':False,
            'SAVE_STYLES':True,
            'SAVE_METADATA':True,
            'SELECTED_FEATURES_ONLY':False,
            'EXPORT_RELATED_LAYERS':False})
        
        packagedLayer = QgsVectorLayer(result["OUTPUT"], f"{date[0].toString('dd/MM/yyyy')} - {date[1].toString('dd/MM/yyyy')}", "ogr")

        if packagedLayer.featureCount() != 0:

            QgsProject.instance().addMapLayer(packagedLayer, False)
            group.addLayer(packagedLayer)
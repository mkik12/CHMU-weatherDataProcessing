import processing
from qgis.core import QgsCoordinateReferenceSystem, QgsFeature, QgsVectorLayer, QgsGeometry, QgsRectangle

def resizeExtent(layer: QgsVectorLayer):
    '''
    This function checks whether the input layer's extent exceeds the extent 
    of the Czech Republic. If it does, the function adjusts it accordingly.
    '''

    resizing = False
    czechExtent = {"xmin": 12.0906046789257982,
                    "ymin": 48.5518057394196774,
                    "xmax": 18.8592214534918803,
                    "ymax": 51.0556707436984283}

    projectedLayer = processing.run("native:reprojectlayer", {'INPUT': layer,
                                                            'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
                                                            'OUTPUT': 'TEMPORARY_OUTPUT'})
    
    layerExtent = projectedLayer['OUTPUT'].extent()
    
    xMin = layerExtent.xMinimum()
    yMin = layerExtent.yMinimum()
    xMax = layerExtent.xMaximum()
    yMax = layerExtent.yMaximum()

    if xMin < czechExtent["xmin"]:
        xMin = czechExtent["xmin"]
        resizing = True

    if yMin < czechExtent["ymin"]:
        yMin = czechExtent["ymin"]
        resizing = True

    if xMax > czechExtent["xmax"]:
        xMax = czechExtent["xmax"]
        resizing = True

    if yMax > czechExtent["ymax"]:
        yMax = czechExtent["ymax"]
        resizing = True

    if resizing == True:
        newLayer = QgsVectorLayer("Polygon?crs=EPSG:4326", "MyVectorLayer", "memory")
        provider = newLayer.dataProvider()

        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromRect(QgsRectangle(xMin, yMin, xMax, yMax)))

        provider.addFeature(feature)
        newLayer.updateExtents()

        return newLayer
    
    else:
        return layer
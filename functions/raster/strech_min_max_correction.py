from qgis.core import(
    QgsRasterLayer,
    QgsRasterBandStats
)

def strechMinMaxCorrection(raster: QgsRasterLayer):
    
    provider = raster.dataProvider()
    stats = provider.bandStatistics(1, QgsRasterBandStats.All)
    print(stats.minimumValue, stats.maximumValue)
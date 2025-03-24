# This is a part of "ČHMÚ - Data o počasí," a QGIS plugin that processes meteorological data published by CHMI.  
# Copyright (C) 2025 by Mikuláš Kadečka - mikulas.kad@seznam.cz  

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
import os
import osgeo
import processing
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsFeatureRequest,
    QgsProcessingFeatureSourceDefinition,
    QgsProject,
    QgsRasterLayer,
    QgsVectorFileWriter,
    QgsVectorLayer,
    QgsCoordinateTransformContext
)

from . import essentials
from . import info
from . import raster
from . import user
from . import utils
from . import validation
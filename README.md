# ČHMÚ/CHMI – Meteorological Data Processing

*Copyright (C) 2025 Mikuláš Kadečka – mikulas.kad@seznam.cz*

This QGIS plugin processes meteorological measurements published by the Czech Hydrometeorological Institute using spatial interpolation methods. To function properly, the tool requires all measurements to be downloaded and formatted correctly.  

You can either download preprocessed datasets from this [webpage](https://drive.google.com/drive/folders/12qYemjNOktYcyJgaK6pPfBqbJCzDAlbV?usp=sharing) or use scripts from this [GitHub repository](https://github.com/mkik12/CHMU-weatherFilesScraper) to automate the download of raw data from the CHMI website and convert them into a format suitable for GIS processing.

## What Results to Expect  

The plugin analyzes the activity of CHMI measuring stations and, based on the specified time interval, groups them into units with the same active periods. These groups serve as input for multiple iterations of spatial interpolation.  

After generating interpolation result rasters, the tool calculates a weighted average, where the weights represent the number of active measuring days for each station group. This approach can produce more accurate results compared to a single iteration of spatial interpolation.  

The tool can generate the following outputs:  

- a **weighted average raster** (mandatory result)  
- **point layers** of stations with the same active period (optional, can be enabled in the plugin’s input parameters) 

## How to Use the Plugin  

1. Install the plugin and either use the scripts to download and preprocess data files from the CHMI webpage or download the preprocessed dataset and extract the root folder.  
2. Start the plugin, go to the **Settings** tab, and set the directory path for the "spatial_data" folder obtained in the first step.  
3. Switch to the **Raster** tab and fill in the primary and secondary parameters.  
4. Click the **Start** button to run the plugin.

## How the Plugin Works


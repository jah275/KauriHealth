# KauriHealth
VEGETATION CLASSIFICATION USING REMOTE SENSING TECHNIQUES

The purpose of these scripts is to identify kauri die-back and how kauri vegetation health has changed over time in the Waitakere Ranges, New Zealand using remotely sensed image data from Landsat-8, Sentinel-2, RapidEye satellites and LiDAR. 

Identify and Create Process chart!	

·	Create tree canopy height model from open source LiDAR

·	Mosaicking of raster tiles by scripting a virtual raster file for the 880 DEM and DSM in RStudio

·	Acquire multispectral satellite data of the region
     
.    Identify kauri trees and how vegetation health has changed over time in the Waitakere Ranges

·	Using each identified kauri tree canopy extent and location, associated various vegetation indices

·	Bridge and analyze the geodatabase from ArcPRO in RStudio creating maps, frequency and density plots highlighting the           differences between years, months and vegetation indices

·	Create plots of the spectral profile differences of the Kauri health between health category ranges

·	Explain variations, clustering patterns and the potential to further monitor kauri dieback disease.


    
     
     
Completed R scripts:

1) Creating virtual raster files for Mosaicking of 440 Digital Surface Model (DSM) and 440 Digital Terrain Model (DTM) tiles from LiDAR .tif files in a folder. 

2) Using the R-ArcGIS Bridge:the arcgisbinding Package from https://github.com/R-ArcGIS/r-bridge

3) Exploring the data through various visualisation and analysis (on-going) 

## To Do:
Explore ARCPRO Script MODEL BUILDER usage
Some sort of Python bridge

Learn machine learning processes of identifying trees/vegetation in python

 1) Gather LiDAR data| DONE |
            
     2) Collect Satelite imagery |have from 2012 to 2019 in landsat-8 30m resolution which is too coarse, RapidEye is daily and 2-5m resolution 
     3)
     4)
     
     ...n) create dataframe for python analysis for making plots/infographics
     n+1) What statistical analysis are we going to do that show:
          a) how kauri vegetation health has changed over time?
          b) explain the relationships between seasonal changes in vegetation indices values.
          c) add a layer showing roads/walking paths/rivers and streams
     

Resources:
1) Install python deep learning frameworks for ArcGIS https://pro.arcgis.com/en/pro-app/help/analysis/image-analyst/install-deep-learning-frameworks.htm

2) ESRI Github page https://github.com/Esri/raster-deep-learning

3) ArcGIS Pro Python reference https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm

4) Discovery Paths https://www.esri.com/en-us/arcgis/products/arcgis-pro/resources

Python Scripts:

Build Plugin ERSI 

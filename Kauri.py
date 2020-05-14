'''This script is for creating code that will:

    open a lidar file
    create dem
    create canopy height model
    highlight trees above a certain height '''



# You need to run this cell to get things setup
%matplotlib inline

import matplotlib.pyplot as plt        # the basic python plotting library
import os                              # a base python package for doing basic operations
import sys                             # a base python package for doing system-related operations
import numpy as np                     # numpy is a numeric python library
import rasterio as rio                 # a raster operation package - good for remote sensing data!
import pandas as pd                    # a data analysis library
import geopandas as gpd                # spatial data analysis (built on top of pandas)
import seaborn as sns                  # another graphing package - nicer graphs
import sklearn                         # a machine learning package
import gdal
import scatter_matrix
import subprocess, glob
import rasterio
from rasterio.merge import merge
from rasterio.plot import show


'''After downloading, moving, and wrangling the data, I'm ready to create a composite image from the three scenes.
First, though, I'll use gdalinfo to inspect the spatial metadata of the scenes.'''

!gdalinfo data/DEM_BB31_1002_2013.tif
!gdalinfo data/DEM_BB31_1003_2013.tif
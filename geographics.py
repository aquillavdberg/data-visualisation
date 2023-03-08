# Data handling
import pandas as pd
import numpy as np
import geopandas as gpd
import json

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.layouts import row, column, gridplot
from bokeh.plotting import figure, show, reset_output
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, ColumnDataSource, CDSView, GroupFilter, TabPanel, Tabs
from bokeh.palettes import brewer
from bokeh.models import HoverTool
from forex_python.converter import CurrencyRates
from datetime import datetime

shapefile = 'ne_110m_admin_0_countries.shp'

#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]#Rename columns.

gdf.columns = ['country', 'country_code', 'geometry']
#gdf.head()

gdf = gdf.drop(gdf.index[159]) #remove Antarctica

#----------------------------------------------------#
#TUTORIAL: Met OBESITY
#----------------------------------------------------#
#"""
datafile = 'obesity.csv'

#Read csv file using pandas
df = pd.read_csv(datafile, names = ['entity', 'code', 'year', 'per_cent_obesity'], skiprows = 1)

#Filter data for year 2016.
df_2016 = df[df['year'] == 2016]

#Merge dataframes gdf and df_2016.
merged = gdf.merge(df_2016, left_on = 'country_code', right_on = 'code')

#Read data to json.
merged_json = json.loads(merged.to_json())

#Convert to String like object.
json_data = json.dumps(merged_json)
print(json_data)

#Input GeoJSON source that contains features for plotting.
geosource = GeoJSONDataSource(geojson = json_data)

#Define a sequential multi-hue color palette.
palette = brewer['YlGnBu'][8]

#Reverse color order so that dark blue is highest obesity.
palette = palette[::-1]

#Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 40)

#Define custom tick labels for color bar.
#tick_labels = {'0': '0%', '5': '5%', '10':'10%', '15':'15%', '20':'20%', '25':'25%', '30':'30%','35':'35%', '40': '>40%'}

#Create color bar. 
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', )#major_label_overrides = tick_labels)

#Create figure object.
p = figure(title = 'Share of adults who are obese, 2016', height = 600 , width = 950, toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#Add patch renderer to figure. 
p.patches('xs','ys', source = geosource,fill_color = {'field' :'per_cent_obesity', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)

#Specify figure layout.
p.add_layout(color_bar, 'below')

output_file('output_file_test.html', 
            title='sales data')  # Render to static HTML, or 
#Display figure inline in Jupyter Notebook.
output_notebook()

#Display figure.
show(p)
#"""

#----------------------------------------------------#
#UITWERKING: met SALES
#----------------------------------------------------#
"""
datafile = 'sales_202106.csv'

df = pd.read_csv(datafile, names = ['Buyer Country', 'Amount (Merchant Currency)'])

#Merge dataframes
merged = gdf.merge(df, left_on='country_code', right_on='Buyer Country')

#Read data to json.
merged_json = json.loads(merged.to_json())

#Convert to String like object.
json_data = json.dumps(merged_json)
print(json_data)

#Input GeoJSON source that contains features for plotting.
geosource = GeoJSONDataSource(geojson = json_data)

#Define a sequential multi-hue color palette.
palette = brewer['YlGnBu'][8]

#Reverse color order so that dark blue is highest obesity.
palette = palette[::-1]

#Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
color_mapper = LinearColorMapper(palette = palette, low = -10.00, high = 100.00)

#Define custom tick labels for color bar.
#tick_labels = {'0.00': '0.00%', '50.00':'50.00%', '100.00':'100.00%'}

#Create color bar. 
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', )#major_label_overrides = tick_labels)

#Create figure object.
p = figure(title = 'Share of adults who are obese, 2016', 
           height = 600 , 
           width = 950, 
           toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#Add patch renderer to figure. 
p.patches('xs','ys', source = geosource,fill_color = {'field' :'Amount (Merchant Currency)', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)#Specify figure layout.
p.add_layout(color_bar, 'below')


# Determine where the visualization will be rendered
output_file('output_file_test.html', 
            title='sales data')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

#Display figure.
show(p)

"""
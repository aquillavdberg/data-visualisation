"""Bokeh Visualization Template

This template is a general outline for turning your data into a 
visualization using Bokeh.
"""

'''[15p] Ratings vs Stability: Can you come up with some Key Performance Indicators (metrics
and scores) that help management understand how the app is doing in terms of stability and
user satisfaction? Visualize them in a nice way. For example, the number of crashes in
correlation with the daily average rating '''

# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.layouts import row, column, gridplot
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, TabPanel, Tabs
from bokeh.plotting import reset_output
from bokeh.models import HoverTool

# Prepare the data
stat_crashes = {6: 'stats_crashes_202106_overview(1).csv',
                7: 'stats_crashes_202107_overview(1).csv',
                8: 'stats_crashes_202108_overview(1).csv',
                9: 'stats_crashes_202109_overview(1).csv',
                10: 'stats_crashes_2021010_overview(1).csv',
                11: 'stats_crashes_2021011_overview(1).csv',
                12: 'stats_crashes_2021012_overview(1).csv'}
stats_ratings_overview = {6: 'stats_ratings_202106_overview(1).csv',
                7: 'stats_ratings_202107_overview(1).csv',
                8: 'stats_ratings_202108_overview(1).csv',
                9: 'stats_ratings_202109_overview(1).csv',
                10: 'stats_ratings_2021010_overview(1).csv',
                11: 'stats_ratings_2021011_overview(1).csv',
                12: 'stats_ratings_2021012_overview(1).csv'}
stats_ratings_country = {6: 'stats_ratings_202106_country(1).csv',
                7: 'stats_ratings_202107_country(1).csv',
                8: 'stats_ratings_202108_country(1).csv',
                9: 'stats_ratings_202109_country(1).csv',
                10: 'stats_ratings_2021010_country(1).csv',
                11: 'stats_ratings_2021011_country(1).csv',
                12: 'stats_ratings_2021012_country(1).csv'}


# Determine where the visualization will be rendered
output_file('Ratings.html', 
            title='ratings vs stability')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

def file_to_pd(lib):
    dfs = [pd.read_csv(lib[key]) for key in lib]
    return dfs

# load csv file
# dfs is list containing dataframes
dfs_crashes = file_to_pd(stat_crashes)
dfs_ratings_country = file_to_pd(stats_ratings_country)
dfs_ratings_overview = file_to_pd(stats_ratings_overview)

# ToDo: find items to filter by



# Assign the panels to Tabs

# Show the tabbed layout


# Use reset_output() between subsequent show() calls, as needed
# reset_output()
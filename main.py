"""Bokeh Visualization Template

This template is a general outline for turning your data into a 
visualization using Bokeh.
"""
# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
# from bokeh.models import ColumnDataSource
# from bokeh.layouts import row, column, gridplot
# from bokeh.models.widgets import Tabs, Panel

# from bokeh.plotting import reset_output

# Prepare the data
# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 2]

# Determine where the visualization will be rendered
output_file('output_file_test.html', 
            title='Empty Bokeh Figure')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

# Set up the figure(s)
fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
            #  plot_height=300,
            #  plot_width=500,
            #  h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location=None,
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             title='Example Figure',
             title_location='right',
             tools='save')
# Remove the gridlines from the figure() object
fig.grid.grid_line_color = None

# Connect to and draw the data
# Draw the coordinates as circles
fig.circle(x=x, y=y,
           color='green', size=10, alpha=0.5)

# Organize the layout

# Preview and save 
show(fig)  # See what I made, and save if I like it

# Use reset_output() between subsequent show() calls, as needed
# reset_output()
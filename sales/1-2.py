import numpy as np
import csv
import pandas as pd
import glob
import os
import pathlib
from pathlib import Path

# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

p = pathlib.Path(__file__).parent.resolve()
all_files = glob.glob(os.path.join(p, "sales\*.csv"))
csvList = []
for filename in all_files:
    if not (filename.endswith('sales_202112.csv') or filename.endswith('sales_202111.csv')):
      df = pd.read_csv(filename, parse_dates=["Transaction Date"])
      df["Amount (Merchant Currency)"] = df.groupby(["Transaction Date"])["Amount (Merchant Currency)"].transform(sum)
      csvList.append(df)
      
frame = pd.concat(csvList, axis=0, ignore_index=True)

sales_cds = ColumnDataSource(frame)  

output_file('first_glyphs.html', title='First Glyphs')

fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Sales in june 2021',
             x_axis_label='Date', y_axis_label='Sales',
             toolbar_location=None)

fig.step('Transaction Date', 'Amount (Merchant Currency)', 
         color='#CE1141', legend_label='Sales', 
         source=sales_cds)

show(fig)
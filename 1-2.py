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
      #df = df.groupby('Transaction Date').count()
      df["Amount (Merchant Currency)"] = df.groupby(["Transaction Date"])["Amount (Merchant Currency)"].transform(sum)
      csvList.append(df)
      
      
frame = pd.concat(csvList, axis=0, ignore_index=True)

dmtoolspf2 = frame[frame['Sku Id'] == 'dmtoolspf2']
charpf2 = frame[frame['Sku Id'] == 'charpf2']
unlockcharactermanager = frame[frame['Sku Id'] == 'unlockcharactermanager']
premium = frame[frame['Sku Id'] == 'premium']

dmtoolspf2_cds = ColumnDataSource(dmtoolspf2)  
charpf2_cds = ColumnDataSource(charpf2) 
unlockcharactermanager_cds = ColumnDataSource(unlockcharactermanager) 
premium_cds = ColumnDataSource(premium) 

output_file('attribute_segmentation_and_filtering.html', title='Attribute Segmentation')



fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Sales in june 2021',
             x_axis_label='Date', y_axis_label='Sales',
             toolbar_location=None)

fig.step('Transaction Date', 'Amount (Merchant Currency)', 
         color='#a52a2a', legend_label='dmtoolspf2', 
         source=dmtoolspf2_cds)
fig.step('Transaction Date', 'Amount (Merchant Currency)', 
         color='#007fff', legend_label='charpf2', 
         source=charpf2_cds)
fig.step('Transaction Date', 'Amount (Merchant Currency)', 
         color='#f4c2c2', legend_label='unlockcharactermanager', 
         source=unlockcharactermanager_cds)
fig.step('Transaction Date', 'Amount (Merchant Currency)', 
         color='#66ff00', legend_label='premium', 
         source=premium_cds)
show(fig)
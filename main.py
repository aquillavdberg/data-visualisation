"""Bokeh Visualization Template

This template is a general outline for turning your data into a 
visualization using Bokeh.
"""

'''[10p] Sales Volume: Visualize the sales over time (for example, per month or per day) in
terms of at least two measures. For example: real money (Amount) and transaction count
(row count). '''

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
# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 2]

# Determine where the visualization will be rendered
output_file('output_file_test.html', 
            title='Empty Bokeh Figure')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

# load csv file
stats_6 = pd.read_csv('sales_202106.csv', parse_dates=['Transaction Date'])
stats_7 = pd.read_csv('sales_202107.csv', parse_dates=['Transaction Date'])
stats_8 = pd.read_csv('sales_202108.csv', parse_dates=['Transaction Date'])
stats_9 = pd.read_csv('sales_202109.csv', parse_dates=['Transaction Date'])
stats_10 = pd.read_csv('sales_202110.csv', parse_dates=['Transaction Date'])
stats_11 = pd.read_csv('sales_202111.csv', parse_dates=['Order Charged Date'])
stats_12 = pd.read_csv('sales_202112.csv', parse_dates=['Order Charged Date'])

# index=dates, columns=['A', 'B', 'C', 'D']

print(stats_6)
# , 'Transaction Type'

# (
stats_6['Amount (Merchant Currency)'] = stats_6.groupby(['Transaction Date'])['Amount (Merchant Currency)'].transform(sum)
#    .loc[:, lambda df: ['Transaction Date', 'Transaction Type', 'Amount (Merchant Currency)'] ])
# print(stats_6)

# Create a ColumnDataSource
stats_6_cds = ColumnDataSource(stats_6)
stats_7_cds = ColumnDataSource(stats_7)
stats_8_cds = ColumnDataSource(stats_8)
stats_9_cds = ColumnDataSource(stats_9)
stats_10_cds = ColumnDataSource(stats_10)
stats_11_cds = ColumnDataSource(stats_11)
stats_12_cds = ColumnDataSource(stats_12)

# west_top_2 = (stats_6[(stats_6['Transaction Type'] == 'Charge') | (stats_6['Transaction Type'] == 'Google fee') | (stats_6['Transaction Type'] == 'Charge refund') | (stats_6['Transaction Type'] == 'Google fee refund')]
#             .loc[:, ['Transaction Date', 'Transaction Type', 'Amount (Merchant Currency)']]
#             .sort_values(['Transaction Type','Transaction Date']))
# west_top_2.head()

# Create the views for transaction type
charge_stats_6_view = CDSView(source=stats_6_cds
                       ,filters=[GroupFilter(column_name='Transaction Type', group='Charge')])
# Google_fee_stats_6_view = CDSView(source=stats_6_cds
#                        ,filters=[GroupFilter(column_name='Transaction Type', group='Google fee')])
Charge_refund_stats_6_view = CDSView(source=stats_6_cds
                       ,filters=[GroupFilter(column_name='Transaction Type', group='Charge refund')])
# Google_fee_refund_stats_6_view = CDSView(source=stats_6_cds
#                        ,filters=[GroupFilter(column_name='Transaction Type', group='Google fee refund')])

# Format the tooltip
tooltips = [
    ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
    ("Transaction Date", "@Transaction Date"),
    # ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Set up the figure(s)
stats_6_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='eu',
                  toolbar_location="below",
                  tools=select_tools,)

stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
              legend_label='charges',
              source=stats_6_cds, view=charge_stats_6_view)

# stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
#               legend_label='Google fees',
#               source=stats_6_cds, view=Google_fee_stats_6_view)

stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
              legend_label='charge refunds',
              source=stats_6_cds, view=Charge_refund_stats_6_view)

# stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
#               legend_label='Google refunds',
#               source=stats_6_cds, view=Google_fee_refund_stats_6_view)

# Create two panels, one for each conference
stats_6_panel = TabPanel(child=stats_6_fig, title="stats of june")  # noqa
# west_panel = TabPanel(child=west_fig, title="Western Conference")  # noqa

# Assign the panels to Tabs
tabs = Tabs(tabs=[stats_6_panel])

# Add square representing each player
stats_6_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source=stats_6_cds,
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_6_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_6_fig.legend.click_policy = "hide"

# Show the tabbed layout
show(tabs)  # noqa

# Use reset_output() between subsequent show() calls, as needed
# reset_output()
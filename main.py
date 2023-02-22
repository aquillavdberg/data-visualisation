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
            title='sales data')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

# load csv file
stats_6 = pd.read_csv('sales_202106.csv', parse_dates=['Transaction Date'], index_col=['Transaction Date'])
stats_7 = pd.read_csv('sales_202107.csv', parse_dates=['Transaction Date'], index_col=['Transaction Date'])


stats_8 = pd.read_csv('sales_202108.csv', parse_dates=['Transaction Date'], index_col=['Transaction Date'])
stats_9 = pd.read_csv('sales_202109.csv', parse_dates=['Transaction Date'], index_col=['Transaction Date'])
stats_10 = pd.read_csv('sales_202110.csv', parse_dates=['Transaction Date'], index_col=['Transaction Date'])
stats_11 = pd.read_csv('sales_202111.csv', parse_dates=['Order Charged Date'], index_col=['Order Charged Date'])
stats_12 = pd.read_csv('sales_202112.csv', parse_dates=['Order Charged Date'], index_col=['Order Charged Date'])

'''
dedicated
aan
file
6:
'''
stats_6_filtered = (stats_6
            .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
            .sort_values(['Transaction Date', 'Transaction Type'])
            )
print("stats_6_filtered")
print(stats_6_filtered)

stats_6_grouped = stats_6_filtered.groupby(['Transaction Date', 'Transaction Type'])

stats_6_sum = stats_6_grouped.sum()['Amount (Merchant Currency)']
# print("stats_6_sum")
# print(stats_6_sum)

stats_6_sum_charge = stats_6_sum.loc[:, 'Charge'].to_frame()
# print("stats_6_sum_charge")
# print(stats_6_sum_charge)

stats_6_sum_Google_fee = stats_6_sum.loc[:, 'Google fee'].to_frame()
# print("stats_6_sum_Google fee")
# print(stats_6_sum_Google_fee)

stats_6_sum_Charge_refund = stats_6_sum.loc[:, 'Charge refund'].to_frame()
# print("stats_6_sum_Charge refund")
# print(stats_6_sum_Charge_refund)

stats_6_sum_Google_refund = stats_6_sum.loc[:, 'Google fee refund'].to_frame()
# print("stats_6_sum_Google_refund")
# print(stats_6_sum_Google_refund)

# Create a ColumnDataSource
stats_6_sum_cds = ColumnDataSource(stats_6_sum.to_frame())
stats_6_sum_charge_cds = ColumnDataSource(stats_6_sum_charge)
stats_6_sum_Google_fee_cds = ColumnDataSource(stats_6_sum_Google_fee)
stats_6_sum_Charge_refund_cds = ColumnDataSource(stats_6_sum_Charge_refund)
stats_6_sum_Google_refund_cds = ColumnDataSource(stats_6_sum_Google_refund)
# stats_7_cds = ColumnDataSource(stats_7)
# stats_8_cds = ColumnDataSource(stats_8)
# stats_9_cds = ColumnDataSource(stats_9)
# stats_10_cds = ColumnDataSource(stats_10)
# stats_11_cds = ColumnDataSource(stats_11)
# stats_12_cds = ColumnDataSource(stats_12)

# Create the views for transaction type
charge_stats_6_view = CDSView(source=stats_6_sum_charge_cds)
Google_fee_stats_6_view = CDSView(source=stats_6_sum_Google_fee_cds)
Charge_refund_stats_6_view = CDSView(source=stats_6_sum_Charge_refund_cds)
Google_fee_refund_stats_6_view = CDSView(source=stats_6_sum_Google_refund_cds)

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
              source=stats_6_sum_charge_cds, view=charge_stats_6_view)

stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
              legend_label='Google fees',
              source=stats_6_sum_Google_fee_cds, view=Google_fee_stats_6_view)

stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
              legend_label='charge refunds',
              source=stats_6_sum_Charge_refund_cds, view=Charge_refund_stats_6_view)

stats_6_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
              legend_label='Google refunds',
              source=stats_6_sum_Google_refund_cds, view=Google_fee_refund_stats_6_view)


# Add square representing each datapoint
stats_6_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source= stats_6_sum_cds, 
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_6_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_6_fig.legend.click_policy = "hide"

# Create two panels, one for each conference
stats_6_panel = TabPanel(child=stats_6_fig, title="stats of june")

'''
dedicated
aan
file
7:
'''

stats_7_filtered = (stats_7
            .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
            .sort_values(['Transaction Date', 'Transaction Type'])
            )
print("stats_7_filtered")
print(stats_7_filtered)

stats_7_grouped = stats_7_filtered.groupby(['Transaction Date', 'Transaction Type'])

stats_7_sum = stats_7_grouped.sum()['Amount (Merchant Currency)']
# print("stats_7_sum")
# print(stats_7_sum)

stats_7_sum_charge = stats_7_sum.loc[:, 'Charge'].to_frame()
# print("stats_7_sum_charge")
# print(stats_7_sum_charge)

stats_7_sum_Google_fee = stats_7_sum.loc[:, 'Google fee'].to_frame()
# print("stats_7_sum_Google fee")
# print(stats_7_sum_Google_fee)

stats_7_sum_Charge_refund = stats_7_sum.loc[:, 'Charge refund'].to_frame()
# print("stats_7_sum_Charge refund")
# print(stats_7_sum_Charge_refund)

stats_7_sum_Google_refund = stats_7_sum.loc[:, 'Google fee refund'].to_frame()
# print("stats_7_sum_Google_refund")
# print(stats_7_sum_Google_refund)

# Create a ColumnDataSource
stats_7_sum_cds = ColumnDataSource(stats_7_sum.to_frame())
stats_7_sum_charge_cds = ColumnDataSource(stats_7_sum_charge)
stats_7_sum_Google_fee_cds = ColumnDataSource(stats_7_sum_Google_fee)
stats_7_sum_Charge_refund_cds = ColumnDataSource(stats_7_sum_Charge_refund)
stats_7_sum_Google_refund_cds = ColumnDataSource(stats_7_sum_Google_refund)
# stats_7_cds = ColumnDataSource(stats_7)
# stats_8_cds = ColumnDataSource(stats_8)
# stats_9_cds = ColumnDataSource(stats_9)
# stats_10_cds = ColumnDataSource(stats_10)
# stats_11_cds = ColumnDataSource(stats_11)
# stats_12_cds = ColumnDataSource(stats_12)

# Create the views for transaction type
charge_stats_7_view = CDSView(source=stats_7_sum_charge_cds)
Google_fee_stats_7_view = CDSView(source=stats_7_sum_Google_fee_cds)
Charge_refund_stats_7_view = CDSView(source=stats_7_sum_Charge_refund_cds)
Google_fee_refund_stats_7_view = CDSView(source=stats_7_sum_Google_refund_cds)

# Format the tooltip
tooltips = [
    ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
    ("Transaction Date", "@Transaction Date"),
    # ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Set up the figure(s)
stats_7_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='eu',
                  toolbar_location="below",
                  tools=select_tools,)

stats_7_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
              legend_label='charges',
              source=stats_7_sum_charge_cds, view=charge_stats_7_view)

stats_7_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
              legend_label='Google fees',
              source=stats_7_sum_Google_fee_cds, view=Google_fee_stats_7_view)

stats_7_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
              legend_label='charge refunds',
              source=stats_7_sum_Charge_refund_cds, view=Charge_refund_stats_7_view)

stats_7_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
              legend_label='Google refunds',
              source=stats_7_sum_Google_refund_cds, view=Google_fee_refund_stats_7_view)


# Add square representing each datapoint
stats_7_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source= stats_7_sum_cds, 
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_7_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_7_fig.legend.click_policy = "hide"

# Create two panels, one for each conference
stats_7_panel = TabPanel(child=stats_7_fig, title="stats of july")




'''
dedicated
aan
file
8:
'''


stats_8_filtered = (stats_8
            .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
            .sort_values(['Transaction Date', 'Transaction Type'])
            )
print("stats_8_filtered")
print(stats_8_filtered)

stats_8_grouped = stats_8_filtered.groupby(['Transaction Date', 'Transaction Type'])

stats_8_sum = stats_8_grouped.sum()['Amount (Merchant Currency)']
# print("stats_8_sum")
# print(stats_8_sum)

stats_8_sum_charge = stats_8_sum.loc[:, 'Charge'].to_frame()
# print("stats_8_sum_charge")
# print(stats_8_sum_charge)

stats_8_sum_Google_fee = stats_8_sum.loc[:, 'Google fee'].to_frame()
# print("stats_8_sum_Google fee")
# print(stats_8_sum_Google_fee)

stats_8_sum_Charge_refund = stats_8_sum.loc[:, 'Charge refund'].to_frame()
# print("stats_8_sum_Charge refund")
# print(stats_8_sum_Charge_refund)

stats_8_sum_Google_refund = stats_8_sum.loc[:, 'Google fee refund'].to_frame()
# print("stats_8_sum_Google_refund")
# print(stats_8_sum_Google_refund)

# Create a ColumnDataSource
stats_8_sum_cds = ColumnDataSource(stats_8_sum.to_frame())
stats_8_sum_charge_cds = ColumnDataSource(stats_8_sum_charge)
stats_8_sum_Google_fee_cds = ColumnDataSource(stats_8_sum_Google_fee)
stats_8_sum_Charge_refund_cds = ColumnDataSource(stats_8_sum_Charge_refund)
stats_8_sum_Google_refund_cds = ColumnDataSource(stats_8_sum_Google_refund)


# Create the views for transaction type
charge_stats_8_view = CDSView(source=stats_8_sum_charge_cds)
Google_fee_stats_8_view = CDSView(source=stats_8_sum_Google_fee_cds)
Charge_refund_stats_8_view = CDSView(source=stats_8_sum_Charge_refund_cds)
Google_fee_refund_stats_8_view = CDSView(source=stats_8_sum_Google_refund_cds)

# Format the tooltip
tooltips = [
    ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
    ("Transaction Date", "@Transaction Date"),
    # ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Set up the figure(s)
stats_8_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='eu',
                  toolbar_location="below",
                  tools=select_tools,)

stats_8_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
              legend_label='charges',
              source=stats_8_sum_charge_cds, view=charge_stats_8_view)

stats_8_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
              legend_label='Google fees',
              source=stats_8_sum_Google_fee_cds, view=Google_fee_stats_8_view)

stats_8_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
              legend_label='charge refunds',
              source=stats_8_sum_Charge_refund_cds, view=Charge_refund_stats_8_view)

stats_8_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
              legend_label='Google refunds',
              source=stats_8_sum_Google_refund_cds, view=Google_fee_refund_stats_8_view)


# Add square representing each datapoint
stats_8_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source= stats_8_sum_cds, 
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_8_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_8_fig.legend.click_policy = "hide"

# Create two panels, one for each conference
stats_8_panel = TabPanel(child=stats_8_fig, title="stats of august")


'''
dedicated
aan
file
9:
'''


stats_9_filtered = (stats_9
            .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
            .sort_values(['Transaction Date', 'Transaction Type'])
            )
print("stats_9_filtered")
print(stats_9_filtered)

stats_9_grouped = stats_9_filtered.groupby(['Transaction Date', 'Transaction Type'])

stats_9_sum = stats_9_grouped.sum()['Amount (Merchant Currency)']
# print("stats_9_sum")
# print(stats_9_sum)

stats_9_sum_charge = stats_9_sum.loc[:, 'Charge'].to_frame()
# print("stats_9_sum_charge")
# print(stats_9_sum_charge)

stats_9_sum_Google_fee = stats_9_sum.loc[:, 'Google fee'].to_frame()
# print("stats_9_sum_Google fee")
# print(stats_9_sum_Google_fee)

stats_9_sum_Charge_refund = stats_9_sum.loc[:, 'Charge refund'].to_frame()
# print("stats_9_sum_Charge refund")
# print(stats_9_sum_Charge_refund)

stats_9_sum_Google_refund = stats_9_sum.loc[:, 'Google fee refund'].to_frame()
# print("stats_9_sum_Google_refund")
# print(stats_9_sum_Google_refund)

# Create a ColumnDataSource
stats_9_sum_cds = ColumnDataSource(stats_9_sum.to_frame())
stats_9_sum_charge_cds = ColumnDataSource(stats_9_sum_charge)
stats_9_sum_Google_fee_cds = ColumnDataSource(stats_9_sum_Google_fee)
stats_9_sum_Charge_refund_cds = ColumnDataSource(stats_9_sum_Charge_refund)
stats_9_sum_Google_refund_cds = ColumnDataSource(stats_9_sum_Google_refund)


# Create the views for transaction type
charge_stats_9_view = CDSView(source=stats_9_sum_charge_cds)
Google_fee_stats_9_view = CDSView(source=stats_9_sum_Google_fee_cds)
Charge_refund_stats_9_view = CDSView(source=stats_9_sum_Charge_refund_cds)
Google_fee_refund_stats_9_view = CDSView(source=stats_9_sum_Google_refund_cds)

# Format the tooltip
tooltips = [
    ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
    ("Transaction Date", "@Transaction Date"),
    # ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Set up the figure(s)
stats_9_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='eu',
                  toolbar_location="below",
                  tools=select_tools,)

stats_9_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
              legend_label='charges',
              source=stats_9_sum_charge_cds, view=charge_stats_9_view)

stats_9_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
              legend_label='Google fees',
              source=stats_9_sum_Google_fee_cds, view=Google_fee_stats_9_view)

stats_9_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
              legend_label='charge refunds',
              source=stats_9_sum_Charge_refund_cds, view=Charge_refund_stats_9_view)

stats_9_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
              legend_label='Google refunds',
              source=stats_9_sum_Google_refund_cds, view=Google_fee_refund_stats_9_view)


# Add square representing each datapoint
stats_9_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source= stats_9_sum_cds, 
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_9_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_9_fig.legend.click_policy = "hide"

# Create two panels, one for each conference
stats_9_panel = TabPanel(child=stats_9_fig, title="stats of septembre")


'''
dedicated
aan
file
10:
'''


stats_10_filtered = (stats_10
            .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
            .sort_values(['Transaction Date', 'Transaction Type'])
            )
print("stats_10_filtered")
print(stats_10_filtered)

stats_10_grouped = stats_10_filtered.groupby(['Transaction Date', 'Transaction Type'])

stats_10_sum = stats_10_grouped.sum()['Amount (Merchant Currency)']
# print("stats_10_sum")
# print(stats_10_sum)

stats_10_sum_charge = stats_10_sum.loc[:, 'Charge'].to_frame()
# print("stats_10_sum_charge")
# print(stats_10_sum_charge)

stats_10_sum_Google_fee = stats_10_sum.loc[:, 'Google fee'].to_frame()
# print("stats_10_sum_Google fee")
# print(stats_10_sum_Google_fee)

stats_10_sum_Charge_refund = stats_10_sum.loc[:, 'Charge refund'].to_frame()
# print("stats_10_sum_Charge refund")
# print(stats_10_sum_Charge_refund)

stats_10_sum_Google_refund = stats_10_sum.loc[:, 'Google fee refund'].to_frame()
# print("stats_10_sum_Google_refund")
# print(stats_10_sum_Google_refund)

# Create a ColumnDataSource
stats_10_sum_cds = ColumnDataSource(stats_10_sum.to_frame())
stats_10_sum_charge_cds = ColumnDataSource(stats_10_sum_charge)
stats_10_sum_Google_fee_cds = ColumnDataSource(stats_10_sum_Google_fee)
stats_10_sum_Charge_refund_cds = ColumnDataSource(stats_10_sum_Charge_refund)
stats_10_sum_Google_refund_cds = ColumnDataSource(stats_10_sum_Google_refund)


# Create the views for transaction type
charge_stats_10_view = CDSView(source=stats_10_sum_charge_cds)
Google_fee_stats_10_view = CDSView(source=stats_10_sum_Google_fee_cds)
Charge_refund_stats_10_view = CDSView(source=stats_10_sum_Charge_refund_cds)
Google_fee_refund_stats_10_view = CDSView(source=stats_10_sum_Google_refund_cds)

# Format the tooltip
tooltips = [
    ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
    ("Transaction Date", "@Transaction Date"),
    # ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Set up the figure(s)
stats_10_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='eu',
                  toolbar_location="below",
                  tools=select_tools,)

stats_10_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
              legend_label='charges',
              source=stats_10_sum_charge_cds, view=charge_stats_10_view)

stats_10_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
              legend_label='Google fees',
              source=stats_10_sum_Google_fee_cds, view=Google_fee_stats_10_view)

stats_10_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007BB7',
              legend_label='charge refunds',
              source=stats_10_sum_Charge_refund_cds, view=Charge_refund_stats_10_view)

stats_10_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
              legend_label='Google refunds',
              source=stats_10_sum_Google_refund_cds, view=Google_fee_refund_stats_10_view)


# Add square representing each datapoint
stats_10_fig.square(
    x="Transaction Date",
    y="Amount (Merchant Currency)",
    source= stats_10_sum_cds, 
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Add the HoverTool to the figure
stats_10_fig.add_tools(HoverTool(tooltips=tooltips))

# Add interactivity to the legend
stats_10_fig.legend.click_policy = "hide"

# Create two panels, one for each conference
stats_10_panel = TabPanel(child=stats_10_fig, title="stats of octobre")


# '''
# dedicated
# aan
# file
# 11:
# '''


# stats_11_filtered = (stats_11
#             .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
#             .sort_values(['Transaction Date', 'Transaction Type'])
#             )
# print("stats_11_filtered")
# print(stats_11_filtered)

# stats_11_grouped = stats_11_filtered.groupby(['Transaction Date', 'Transaction Type'])

# stats_11_sum = stats_11_grouped.sum()['Amount (Merchant Currency)']
# # print("stats_11_sum")
# # print(stats_11_sum)

# stats_11_sum_charge = stats_11_sum.loc[:, 'Charge'].to_frame()
# # print("stats_11_sum_charge")
# # print(stats_11_sum_charge)

# stats_11_sum_Google_fee = stats_11_sum.loc[:, 'Google fee'].to_frame()
# # print("stats_11_sum_Google fee")
# # print(stats_11_sum_Google_fee)

# stats_11_sum_Charge_refund = stats_11_sum.loc[:, 'Charge refund'].to_frame()
# # print("stats_11_sum_Charge refund")
# # print(stats_11_sum_Charge_refund)

# stats_11_sum_Google_refund = stats_11_sum.loc[:, 'Google fee refund'].to_frame()
# # print("stats_11_sum_Google_refund")
# # print(stats_11_sum_Google_refund)

# # Create a ColumnDataSource
# stats_11_sum_cds = ColumnDataSource(stats_11_sum.to_frame())
# stats_11_sum_charge_cds = ColumnDataSource(stats_11_sum_charge)
# stats_11_sum_Google_fee_cds = ColumnDataSource(stats_11_sum_Google_fee)
# stats_11_sum_Charge_refund_cds = ColumnDataSource(stats_11_sum_Charge_refund)
# stats_11_sum_Google_refund_cds = ColumnDataSource(stats_11_sum_Google_refund)


# # Create the views for transaction type
# charge_stats_11_view = CDSView(source=stats_11_sum_charge_cds)
# Google_fee_stats_11_view = CDSView(source=stats_11_sum_Google_fee_cds)
# Charge_refund_stats_11_view = CDSView(source=stats_11_sum_Charge_refund_cds)
# Google_fee_refund_stats_11_view = CDSView(source=stats_11_sum_Google_refund_cds)

# # Format the tooltip
# tooltips = [
#     ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
#     ("Transaction Date", "@Transaction Date"),
#     # ("Three-Point Percentage", "@pct3PM{00.0%}"),
# ]

# # Specify the selection tools to be made available
# select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# # Set up the figure(s)
# stats_11_fig = figure(x_axis_type='datetime',
#                   height=300,
#                   x_axis_label='Date',
#                   y_axis_label='eu',
#                   toolbar_location="below",
#                   tools=select_tools,)

# stats_11_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
#               legend_label='charges',
#               source=stats_11_sum_charge_cds, view=charge_stats_11_view)

# stats_11_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1141',
#               legend_label='Google fees',
#               source=stats_11_sum_Google_fee_cds, view=Google_fee_stats_11_view)

# stats_11_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
#               legend_label='charge refunds',
#               source=stats_11_sum_Charge_refund_cds, view=Charge_refund_stats_11_view)

# stats_11_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
#               legend_label='Google refunds',
#               source=stats_11_sum_Google_refund_cds, view=Google_fee_refund_stats_11_view)


# # Add square representing each datapoint
# stats_11_fig.square(
#     x="Transaction Date",
#     y="Amount (Merchant Currency)",
#     source= stats_11_sum_cds, 
#     color="royalblue",
#     selection_color="deepskyblue",
#     nonselection_color="lightgray",
#     nonselection_alpha=0.3,
# )

# # Add the HoverTool to the figure
# stats_11_fig.add_tools(HoverTool(tooltips=tooltips))

# # Add interactivity to the legend
# stats_11_fig.legend.click_policy = "hide"

# # Create two panels, one for each conference
# stats_11_panel = TabPanel(child=stats_11_fig, title="stats of novembre")


# '''
# dedicated
# aan
# file
# 12:
# '''


# stats_12_filtered = (stats_12
#             .loc[:, ['Transaction Type', 'Amount (Merchant Currency)']]
#             .sort_values(['Transaction Date', 'Transaction Type'])
#             )
# print("stats_12_filtered")
# print(stats_12_filtered)

# stats_12_grouped = stats_12_filtered.groupby(['Transaction Date', 'Transaction Type'])

# stats_12_sum = stats_12_grouped.sum()['Amount (Merchant Currency)']
# # print("stats_12_sum")
# # print(stats_12_sum)

# stats_12_sum_charge = stats_12_sum.loc[:, 'Charge'].to_frame()
# # print("stats_12_sum_charge")
# # print(stats_12_sum_charge)

# stats_12_sum_Google_fee = stats_12_sum.loc[:, 'Google fee'].to_frame()
# # print("stats_12_sum_Google fee")
# # print(stats_12_sum_Google_fee)

# stats_12_sum_Charge_refund = stats_12_sum.loc[:, 'Charge refund'].to_frame()
# # print("stats_12_sum_Charge refund")
# # print(stats_12_sum_Charge_refund)

# stats_12_sum_Google_refund = stats_12_sum.loc[:, 'Google fee refund'].to_frame()
# # print("stats_12_sum_Google_refund")
# # print(stats_12_sum_Google_refund)

# # Create a ColumnDataSource
# stats_12_sum_cds = ColumnDataSource(stats_12_sum.to_frame())
# stats_12_sum_charge_cds = ColumnDataSource(stats_12_sum_charge)
# stats_12_sum_Google_fee_cds = ColumnDataSource(stats_12_sum_Google_fee)
# stats_12_sum_Charge_refund_cds = ColumnDataSource(stats_12_sum_Charge_refund)
# stats_12_sum_Google_refund_cds = ColumnDataSource(stats_12_sum_Google_refund)


# # Create the views for transaction type
# charge_stats_12_view = CDSView(source=stats_12_sum_charge_cds)
# Google_fee_stats_12_view = CDSView(source=stats_12_sum_Google_fee_cds)
# Charge_refund_stats_12_view = CDSView(source=stats_12_sum_Charge_refund_cds)
# Google_fee_refund_stats_12_view = CDSView(source=stats_12_sum_Google_refund_cds)

# # Format the tooltip
# tooltips = [
#     ("Amount (Merchant Currency)", "@Amount (Merchant Currency)"),
#     ("Transaction Date", "@Transaction Date"),
#     # ("Three-Point Percentage", "@pct3PM{00.0%}"),
# ]

# # Specify the selection tools to be made available
# select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# # Set up the figure(s)
# stats_12_fig = figure(x_axis_type='datetime',
#                   height=300,
#                   x_axis_label='Date',
#                   y_axis_label='eu',
#                   toolbar_location="below",
#                   tools=select_tools,)

# stats_12_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007A33',
#               legend_label='charges',
#               source=stats_12_sum_charge_cds, view=charge_stats_12_view)

# stats_12_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#CE1241',
#               legend_label='Google fees',
#               source=stats_12_sum_Google_fee_cds, view=Google_fee_stats_12_view)

# stats_12_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#006BB6',
#               legend_label='charge refunds',
#               source=stats_12_sum_Charge_refund_cds, view=Charge_refund_stats_12_view)

# stats_12_fig.step('Transaction Date', 'Amount (Merchant Currency)', color='#007B43',
#               legend_label='Google refunds',
#               source=stats_12_sum_Google_refund_cds, view=Google_fee_refund_stats_12_view)


# # Add square representing each datapoint
# stats_12_fig.square(
#     x="Transaction Date",
#     y="Amount (Merchant Currency)",
#     source= stats_12_sum_cds, 
#     color="royalblue",
#     selection_color="deepskyblue",
#     nonselection_color="lightgray",
#     nonselection_alpha=0.3,
# )

# # Add the HoverTool to the figure
# stats_12_fig.add_tools(HoverTool(tooltips=tooltips))

# # Add interactivity to the legend
# stats_12_fig.legend.click_policy = "hide"

# # Create two panels, one for each conference
# stats_12_panel = TabPanel(child=stats_12_fig, title="stats of decembre")




# Assign the panels to Tabs
tabs = Tabs(tabs=[stats_6_panel, stats_7_panel, stats_8_panel, stats_9_panel, stats_10_panel])

# Show the tabbed layout
show(tabs)  # noqa

# Use reset_output() between subsequent show() calls, as needed
# reset_output()
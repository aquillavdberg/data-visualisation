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
output_file('sales_volume.html', 
            title='sales data')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

def figure_renderer(csv_file, parse_date, index_collumn):
    stats_6 = pd.read_csv(csv_file, parse_dates=[parse_date], index_col=[index_collumn])
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
    if (csv_file == 'sales_202106.csv'):
        stats_6_panel = TabPanel(child=stats_6_fig, title="stats of june")
    elif (csv_file == 'sales_202107.csv'):
        stats_6_panel = TabPanel(child=stats_6_fig, title="stats of july")
    elif (csv_file == 'sales_202108.csv'):
        stats_6_panel = TabPanel(child=stats_6_fig, title="stats of august")
    elif (csv_file == 'sales_202109.csv'):
        stats_6_panel = TabPanel(child=stats_6_fig, title="stats of septembre")
    elif (csv_file == 'sales_202110.csv'):
        stats_6_panel = TabPanel(child=stats_6_fig, title="stats of octobre")
    # elif (csv_file == 'sales_202111.csv'):
    #     stats_6_panel = TabPanel(child=stats_6_fig, title="stats of novembre")
    # elif (csv_file == 'sales_202112.csv'):
    #     stats_6_panel = TabPanel(child=stats_6_fig, title="stats of decembre")
    return stats_6_panel


stats_6_panel = figure_renderer('sales_202106.csv', 'Transaction Date', 'Transaction Date')
stats_7_panel = figure_renderer('sales_202107.csv', 'Transaction Date', 'Transaction Date')
stats_8_panel = figure_renderer('sales_202108.csv', 'Transaction Date', 'Transaction Date')
stats_9_panel = figure_renderer('sales_202109.csv', 'Transaction Date', 'Transaction Date')
stats_10_panel = figure_renderer('sales_202110.csv', 'Transaction Date', 'Transaction Date')

# load csv file
stats_11 = pd.read_csv('sales_202111.csv', parse_dates=['Order Charged Date'], index_col=['Order Charged Date'])
stats_12 = pd.read_csv('sales_202112.csv', parse_dates=['Order Charged Date'], index_col=['Order Charged Date'])


# Assign the panels to Tabs
tabs = Tabs(tabs=[stats_6_panel, stats_7_panel, stats_8_panel, stats_9_panel, stats_10_panel])

# Show the tabbed layout
show(tabs)  # noqa

# Use reset_output() between subsequent show() calls, as needed
# reset_output()
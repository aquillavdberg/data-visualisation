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
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, TabPanel, Tabs, Select, CustomJS
from bokeh.plotting import reset_output
from bokeh.models import HoverTool

# Prepare the data
stat_crashes = {6: 'stats_crashes_202106_overview(1).csv',
                7: 'stats_crashes_202107_overview(1).csv',
                8: 'stats_crashes_202108_overview(1).csv',
                9: 'stats_crashes_202109_overview(1).csv',
                10: 'stats_crashes_202110_overview(1).csv',
                11: 'stats_crashes_202111_overview(1).csv',
                12: 'stats_crashes_202112_overview(1).csv'}
stats_ratings_overview = {6: 'stats_ratings_202106_overview(1).csv',
                7: 'stats_ratings_202107_overview(1).csv',
                8: 'stats_ratings_202108_overview(1).csv',
                9: 'stats_ratings_202109_overview(1).csv',
                10: 'stats_ratings_202110_overview(1).csv',
                11: 'stats_ratings_202111_overview(1).csv',
                12: 'stats_ratings_202112_overview(1).csv'}
stats_ratings_country = {6: 'stats_ratings_202106_country(1).csv',
                7: 'stats_ratings_202107_country(1).csv',
                8: 'stats_ratings_202108_country(1).csv',
                9: 'stats_ratings_202109_country(1).csv',
                10: 'stats_ratings_202110_country(1).csv',
                11: 'stats_ratings_202111_country(1).csv',
                12: 'stats_ratings_202112_country(1).csv'}

list_of_countries = ['AR', 'AT', 'AU', 'BA', 'BD', 'BE', 'BG', 'BH', 'BN', 'BR', 'BW', 'BY', 'CA', 'CH'
 'CL', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'EG', 'ES', 'FI'
 'FR', 'GB', 'GR', 'GT', 'HK', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS'
 'IT', 'JM', 'JP', 'KR', 'KW', 'LB', 'LT', 'LU', 'LV', 'LY', 'MD', 'MT', 'MX', 'MY'
 'MZ', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PR', 'PT', 'PW', 'PY'
 'RO', 'RS', 'RU', 'SE', 'SG', 'SI', 'SK', 'SV', 'TH', 'TR', 'TW', 'UA', 'US', 'UY'
 'VE', 'VN', 'ZA']


# Determine where the visualization will be rendered
output_file('Ratings.html', 
            title='ratings vs stability')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

def file_to_pd(lib):
    dfs = [pd.read_csv(lib[key], parse_dates=['Date'], index_col=['Date']) for key in lib]
    df = pd.concat(dfs)
    return df


# load csv file
# crashes contains daily crashes en daily anr (when the main thread can't process user input/output an updated ui)
df_crashes = file_to_pd(stat_crashes)
# country contains the different countries, daily average rating & total average rating
df_ratings_country = file_to_pd(stats_ratings_country)
# overview contains daily average rating & total average rating
df_ratings_overview = file_to_pd(stats_ratings_overview)


'''
country_panel_list = []
for country in list_of_countries:
    # print(countrie)
    country_cds = ColumnDataSource(df_ratings_country.loc[df_ratings_country["Country"] == country])
    country_view = CDSView(source=country_cds)
    country_fig = figure(x_axis_type='datetime',
                    height=300,
                    x_axis_label='Date',
                    y_axis_label='Rating',)
    country_fig.step('Date', 'Total Average Rating', color='#007A33',
                legend_label=country,
                source=country_cds, view=country_view)
    country_fig.legend.click_policy = "hide"
    country_panel_list.append(TabPanel(child=country_fig, title=country))


# Assign the panels to Tabs
tabs = Tabs(tabs = country_panel_list)
'''

def file_to_pd(lib):
    dfs = [pd.read_csv(lib[key], parse_dates=['Date'], index_col=['Date']) for key in lib]
    df = pd.concat(dfs)
    return df

def render(country):
    country_fig.step('Date', 'Total Average Rating', color='#007A33',
                    legend_label=country,
                    source=country_panel_list[country][0], view=country_panel_list[country][1])
    return country_fig


df_ratings_country = file_to_pd(stats_ratings_country)

# Determine where the visualization will be rendered
output_file('Country.html', 
            title='Country')  # Render to static HTML, or 
output_notebook()  # Render inline in a Jupyter Notebook

# Set up the figure(s)

country_fig = figure(x_axis_type='datetime',
                height=300,
                x_axis_label='Date',
                y_axis_label='Rating',)

country_panel_list = {}
for country in list_of_countries:
    # print(countrie)
    country_cds = ColumnDataSource(df_ratings_country.loc[df_ratings_country["Country"] == country])
    country_view = CDSView(source=country_cds)
    country_panel_list[country] = [country_cds, country_view]


# country_fig.legend.click_policy = "hide"
menu = Select(title="Countries", value="AR", options=list_of_countries)
# menu.js_link('value', country_fig)
menu.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))

def callback(attr, old, new):
    for country in list_of_countries:
        if menu.value == country:
            reset_output()
            show(row(children =[menu, render(country)]))

# Set up the figure(s)
Crashes_fig = figure(x_axis_type='datetime',
                    height=300,
                    x_axis_label='Date',
                    y_axis_label='crashes',)

Daily_Crashes_cds = ColumnDataSource(df_crashes.loc[:, ['Daily Crashes']])
Daily_Crashes_view = CDSView(source=Daily_Crashes_cds)
Crashes_fig.step('Date', 'Daily Crashes', color='#fc0000',
                legend_label='Daily Crashes',
                source=Daily_Crashes_cds, view=Daily_Crashes_view)

Daily_ANRs_cds = ColumnDataSource(df_crashes.loc[:, ['Daily ANRs']])
Daily_ANRs_view = CDSView(source=Daily_ANRs_cds)
Crashes_fig.step('Date', 'Daily ANRs', color='#fc7100',
                legend_label='Daily ANRs',
                source=Daily_ANRs_cds, view=Daily_ANRs_view)
# Assign the panels to Tabs
# tabs = Tabs(tabs = [Daily_Crashes_panel, Daily_ANRs_panel])
Crashes_fig.legend.click_policy = "hide"


Ratings_fig = figure(x_axis_type='datetime',
                    height=300,
                    x_axis_label='Date',
                    y_axis_label='Rating',)

# Set up the figure(s)
Ratings_fig = figure(x_axis_type='datetime',
                    height=300,
                    x_axis_label='Date',
                    y_axis_label='crashes',)

Daily_Rating_cds = ColumnDataSource(df_ratings_overview.loc[:, ['Daily Average Rating']])
Daily_Rating_view = CDSView(source=Daily_Rating_cds)
Ratings_fig.step('Date', 'Daily Average Rating', color='#00ff00',
                legend_label='Daily Average Rating',
                # size=3, alpha=0.5,
                source=Daily_Rating_cds, view=Daily_Rating_view)

Total_Rating_cds = ColumnDataSource(df_ratings_overview.loc[:, ['Total Average Rating']])
Total_Rating_view = CDSView(source=Total_Rating_cds)
Ratings_fig.step('Date', 'Total Average Rating', color='#056605',
                legend_label='Total Average Rating',
                source=Total_Rating_cds, view=Total_Rating_view)

Ratings_fig.legend.click_policy = "hide"

# filter by daily vs total
# 2 grahps onder elkaar:
# 1 voor overview (met aan/uit klikbare daily & total),
# 1 voor country (met aan/uit klikbare daily & total)

# Plot the two visualizations in a vertical configuration
show(row(column(Crashes_fig, Ratings_fig), row(children =[menu, render("AR")])))

# Use reset_output() between subsequent show() calls, as needed
# reset_output()
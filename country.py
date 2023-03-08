# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.layouts import row, column, gridplot
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, Dropdown, ColumnDataSource, CDSView, GroupFilter, TabPanel, Tabs, Button, RadioButtonGroup, Select, Slider
from bokeh.plotting import reset_output
from bokeh.models import HoverTool

list_of_countries = ['AR', 'AT', 'AU', 'BA', 'BD', 'BE', 'BG', 'BH', 'BN', 'BR', 'BW', 'BY', 'CA', 'CH'
 'CL', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'EG', 'ES', 'FI'
 'FR', 'GB', 'GR', 'GT', 'HK', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS'
 'IT', 'JM', 'JP', 'KR', 'KW', 'LB', 'LT', 'LU', 'LV', 'LY', 'MD', 'MT', 'MX', 'MY'
 'MZ', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PR', 'PT', 'PW', 'PY'
 'RO', 'RS', 'RU', 'SE', 'SG', 'SI', 'SK', 'SV', 'TH', 'TR', 'TW', 'UA', 'US', 'UY'
 'VE', 'VN', 'ZA']


stats_ratings_country = {6: 'stats_ratings_202106_country(1).csv',
                7: 'stats_ratings_202107_country(1).csv',
                8: 'stats_ratings_202108_country(1).csv',
                9: 'stats_ratings_202109_country(1).csv',
                10: 'stats_ratings_202110_country(1).csv',
                11: 'stats_ratings_202111_country(1).csv',
                12: 'stats_ratings_202112_country(1).csv'}

def file_to_pd(lib):
    dfs = [pd.read_csv(lib[key], parse_dates=['Date'], index_col=['Date']) for key in lib]
    df = pd.concat(dfs)
    return df

def render(country):
    country_fig.step('Date', 'Total Average Rating', color='#007A33',
                    legend_label=country,
                    source=country_panel_list[country][0], view=country_panel_list[country][1])
    return country_fig

def update(attrname, old, new):
    reset_output()
    show(row(children =[menu, render(menu.value)]))

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
# menu.on_change('value', update)
menu.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))



# Assign the panels to Tabs
# tabs = Tabs(tabs = country_panel_list)

# Show the tabbed layout
show(row(children =[menu, render("AR")]))

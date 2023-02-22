# Bokeh library
# from bokeh.plotting import show
from bokeh.io import output_file
from bokeh.layouts import column
from bokeh.plotting import figure, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Read the csv files
player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv('2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv('2017-18_standings.csv', parse_dates=['stDate'])

west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
               .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
               .sort_values(['teamAbbr','stDate']))
west_top_2.head()

east_top_2 = (standings[(standings['teamAbbr'] == 'BOS') | (standings['teamAbbr'] == 'TOR')]
               .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
               .sort_values(['teamAbbr','stDate']))
east_top_2.head()


rockets_data = west_top_2[west_top_2["teamAbbr"] == "HOU"]  # noqa
warriors_data = west_top_2[west_top_2["teamAbbr"] == "GS"]  # noqa

celtics_data = east_top_2[east_top_2["teamAbbr"] == "BOS"]  # noqa
raptors_data = east_top_2[east_top_2["teamAbbr"] == "TOR"]  # noqa

# Create a ColumnDataSource object for each team
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

celtics_cds = ColumnDataSource(celtics_data)
raptors_cds = ColumnDataSource(raptors_data)

# Output to file
output_file(
    "east-west-top-2-standings-race.html",
    title="Conference Top 2 Teams Wins Race",
)

# Create and configure the figure
east_fig = figure(
    x_axis_type="datetime",
    height=300,
    width=600,
    title="Eastern Conference Top 2 Teams Wins Race, 2017-18",
    x_axis_label="Date",
    y_axis_label="Wins",
    toolbar_location=None,
)

# Render the race as step lines
east_fig.step(
    "stDate",
    "gameWon",
    color="#007A33",
    legend_label="Celtics",
    source=celtics_cds,
)
east_fig.step(
    "stDate",
    "gameWon",
    color="#CE1141",
    legend_label="Raptors",
    source=raptors_cds,
)

# Create and configure the figure
west_fig = figure(
    x_axis_type="datetime",
    height=300,
    width=600,
    title="Western Conference Top 2 Teams Wins Race, 2017-18",
    x_axis_label="Date",
    y_axis_label="Wins",
    toolbar_location=None,
)

# Render the race as step lines
west_fig.step(
    "stDate",
    "gameWon",
    color="#CE1141",
    legend_label="Rockets",
    source=rockets_cds
)
west_fig.step(
    "stDate",
    "gameWon",
    color="#006BB6",
    legend_label="Warriors",
    source=warriors_cds,
)



# Plot the two visualizations in a vertical configuration
show(column(west_fig, east_fig))  # noqa

from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import DatetimeTickFormatter, HoverTool, Range1d
from datetime import datetime, timedelta


def main_plot(query):
    # hover = HoverTool(tooltips=[("Date", "$x"),("Value", "$y")], formatters={"Date": "datetime"}, mode='vline')
    c_tools = ['pan', 'wheel_zoom', 'save', 'reset']
    c = figure(x_axis_type="datetime", title="OSfrog mentions over time", tools=c_tools, logo=None, height=300,
               active_scroll='wheel_zoom')
    c.title.align = "center"
    c.background_fill_color = (238, 238, 238)
    c.background_fill_alpha = 0.1
    c.border_fill_color = (238, 238, 238)
    c.border_fill_alpha = 0.1
    c.xgrid.grid_line_color = "black"
    c.xgrid.grid_line_alpha = 0.3
    c.ygrid.grid_line_color = "black"
    c.ygrid.grid_line_alpha=0.2
    c.toolbar_location = None
    c.xaxis.formatter = DatetimeTickFormatter(days=['%y-%m-%d'])
    # c.line(x=[item[0] for item in query],
    #        y=[item[1] for item in query],
    #        line_width=2,
    #        color=(51, 122, 183),
    #        alpha=1)
    c.circle(x=[item[0] for item in query],
             y=[item[1] for item in query],
             size=10,
             color=(51, 122, 183),
             fill_color=(50, 150, 183),
             alpha=1,
             line_width=2)
    return components(c)


def person_plot(query, name, count):
    # hover = HoverTool(tooltips=[("Date", "$x"), ("Value", "$y")], formatters={"Date": "datetime"}, mode='vline')
    c_tools = ['pan', 'wheel_zoom', 'save', 'reset']
    title_str = "OSfrog mentions over time by " + name
    c = figure(x_axis_type="datetime", title=title_str, tools=c_tools, logo=None, height=300,
               active_scroll='wheel_zoom')
    c.title.align = "center"
    c.background_fill_color = (238, 238, 238)
    c.background_fill_alpha = 0.1
    c.border_fill_color = (238, 238, 238)
    c.border_fill_alpha = 0.1
    c.xgrid.grid_line_color = "black"
    c.xgrid.grid_line_alpha = 0.3
    c.ygrid.grid_line_color = "black"
    c.ygrid.grid_line_alpha = 0.2
    c.toolbar_location = None
    print(type(count), count)
    if count <= 1:
        c.x_range = Range1d(query[0][0] - timedelta(days=2), query[0][0] + timedelta(days=2))

    c.xaxis.formatter = DatetimeTickFormatter(days=['%y-%m-%d'])
    # c.line(x=[item[0] for item in query],
    #        y=[item[1] for item in query],
    #        line_width=2,
    #        color=(51, 122, 183),
    #        alpha=1)
    c.circle(x=[item[0] for item in query],
             y=[item[1] for item in query],
             size=10,
             color=(51, 122, 183),
             fill_color=(50, 150, 183),
             alpha=1,
             line_width=2)
    return components(c)

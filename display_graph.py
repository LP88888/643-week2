"""This module creates a line graph of Toronto's average
mean temperatures, degrees Celsius, in 2017 and 2022"""
import pandas as pd
import altair as alt

def create_chart(df):
    """
    :param df: the dataframe of the data source
    :return: Altair chart

    """

    # Define a dictionary for mapping month to color 
    # [December, January, February = Winter] [March, April, May = Spring] [June, July, August = Summer] [September, October, November = Fall]
    label_colors = {
        'condition': [
            {'test' : 'datum.label == "1"', 'value': 'black'},
            {'test' : 'datum.label == "2"', 'value': 'black'},
            {'test' : 'datum.label == "3"', 'value': 'green'},
            {'test' : 'datum.label == "4"', 'value': 'green'},
            {'test' : 'datum.label == "5"', 'value': 'green'},
            {'test' : 'datum.label == "6"', 'value': 'blue'},
            {'test' : 'datum.label == "7"', 'value': 'blue'},
            {'test' : 'datum.label == "8"', 'value': 'blue'},
            {'test' : 'datum.label == "9"', 'value': 'orange'},
            {'test' : 'datum.label == "10"', 'value': 'orange'},
            {'test' : 'datum.label == "11"', 'value': 'orange'}],
        'value': 'black'}  # The default value if no condition is met (e.g. 12 December)

    # Generate a line plot in Altair showing the month and average mean temperatures
    base = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Month:O", title="Month", axis=alt.Axis(labelAngle=0, tickSize=8, labelFontSize=11, labelFontWeight=500,labelColor=label_colors)),
        y=alt.Y("value", title="Temperature  (C)", axis=alt.Axis(tickSize=8, labelFontSize=11, labelFontWeight=500)),
        color=alt.Color("variable:N", title="Legend"),
        tooltip=["value:Q"], #info for the dots when user hovers there
    )

    # Add text labels, offset text by 25 pixels above each line so they are visible
    labels = base.mark_text(dy = -25).encode(  
        text = alt.Text("value", format=".1f"), # Round temperature to nearest decimal place   
    )

    # Combine and layer the line chart and text labels
    chart = (base + labels).properties(
        title = alt.TitleParams(
            text = "Average Max and Min Temperatures of 2022",
            fontSize = 20,
            fontWeight = 'bold',
            anchor = 'start', #left align the chart title
            subtitle = 'In Toronto, ON, Canada',
            subtitleFontSize = 14,
            subtitleFontWeight = 500,
            dy = -10
        )    
    ).properties(
        width=400,
        height=500
    ).configure(
        background = "#f0f0f0"
    ).configure_axis(
        grid = False
    ).configure_legend(
        labelFontSize=12   # Adjust legend label font size
    )
 
    return chart

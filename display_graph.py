"""
This module creates a line graph of Toronto's average
max and min temperatures in degrees Celsius, in 2022
"""
import pandas as pd
import altair as alt

def create_chart(df):
    """
    This function takes in a df and produces the line chart
    :param df: the dataframe of the data source
    :return: Altair chart

    """

    base = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X(
            "Month:O", 
            title="Month", 
            axis=alt.Axis(labelAngle=0, tickSize=8, labelFontSize=11, labelFontWeight=500)
        ),
        y=alt.Y(
            "value", 
            title="Temperature  (C)", 
            axis=alt.Axis(tickSize=8, labelFontSize=11, labelFontWeight=500)
        ),
        color=alt.Color("variable:N", title="Legend"),
        tooltip=["value:Q"], 
    )

    # Add text labels, offset text by 25 pixels above each line so they are visible
    labels = base.mark_text(dy = -25).encode(  
        text = alt.Text("value", format=".1f"),    
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
        labelFontSize=12   
    )
 
    return chart

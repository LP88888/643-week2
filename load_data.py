"""This module Loads the weather csv into a dataframe and cleans it"""
import pandas as pd 

def load_df(path):
    """
    :param path: the csv file path to the data source
    :return: Dataframe

    """
    df2022 = pd.read_csv(path, usecols=["Date/Time","Month","Mean Temp (°C)","Min Temp (°C)","Max Temp (°C)"])
    df2022 = df2022.dropna()

    # Convert the "Date/Time" column to a datetime object and extract the month from "Date/Time"
    df2022['Date/Time'] = pd.to_datetime(df2022['Date/Time'])
    df2022['Month'] = df2022['Date/Time'].dt.month

    # Group the data by month and calculate the mean of "Mean Temp (°C)","Min Temp (°C)","Max Temp (°C)"
    avg2022 = df2022.groupby("Month").agg(   
        Avg_Max_Temp_2022 = pd.NamedAgg(column = "Max Temp (°C)", aggfunc = "mean"), 
        Avg_Min_Temp_2022 = pd.NamedAgg(column = "Min Temp (°C)", aggfunc = "mean"), 
    ).reset_index()

    # Convert wide form data to long form so it works better with Altair
    avg2022 = avg2022.melt("Month")

    return avg2022


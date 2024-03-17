"""
This module Loads the weather csv into a dataframe and cleans it
"""
import pandas as pd 

def load_df(path):
    """
    Loads the csv from a file path into a dataframe

    :param path: the csv file path to the data source
    :return: the loaded dataframe

    """
    df = pd.read_csv(path)
    return df

def clean_df(df):
    """
    Processes the dataframe by removing N/A, fixing date/time,
    and produces a dataframe with temperatures grouped by month

    :param df: the input dataframe that was loaded
    :return: cleaned and formatted dataframe

    """
    df_2022 = df.dropna()

    # Convert the "Date/Time" column to a datetime object and extract the month from "Date/Time"
    df_2022['Date/Time'] = pd.to_datetime(df_2022['Date/Time'])
    df_2022['Month'] = df_2022['Date/Time'].dt.month

    # Group the data by month and calculate the mean of "Mean Temp (°C)","Min Temp (°C)","Max Temp (°C)"
    df_avg_2022 = df_2022.groupby("Month").agg(   
        Avg_Max_Temp_2022 = pd.NamedAgg(column = "Max Temp (°C)", aggfunc = "mean"), 
        Avg_Min_Temp_2022 = pd.NamedAgg(column = "Min Temp (°C)", aggfunc = "mean"), 
    ).reset_index()

    # Convert wide form data to long form so it works better with Altair
    df_avg_2022 = df_avg_2022.melt("Month")

    return df_avg_2022


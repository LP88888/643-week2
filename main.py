"""
Main function that runs the script, takes in a dataset
and cleans it, and outputs the visualization 
"""
import sys
import load_data
import display_graph
import pip
import argparse

def install(package):
    """
    This function installs the required packages
    param package: the package that needs to be installed
    """
    if hasattr(pip, "main"):
        pip.main(["install", package])
    else:
        pip._internal.main(["install", package])

if __name__ == '__main__':
    install("numpy==1.23.5")
    install("pandas==1.5.3")
    install("altair==4.2.2")
    install("altair_viewer")

    import numpy as np
    import pandas as pd
    import altair as alt
    import altair_viewer

    parser=argparse.ArgumentParser()
    parser.add_argument('first_path', help="TorontoWeather2022.csv")
    args=parser.parse_args()

    original_df = load_data.load_df(args.first_path)
    cleaned_df = load_data.clean_df(original_df)
    line_graph = display_graph.create_chart(cleaned_df)
    altair_viewer.show(line_graph)

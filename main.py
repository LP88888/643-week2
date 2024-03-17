"""This is the main module that takes in a dataset and cleans it """
import sys
import load_data
import display_graph
import pip
import argparse

def install(pkg):
    """
    :param pkg: the package that is to be installed
    """
    if hasattr(pip, "main"):
        pip.main(["install", pkg])
    else:
        pip._internal.main(["install", pkg])

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
    df = load_data.load_df(args.first_path)
    line_graph = display_graph.create_chart(df)
    altair_viewer.show(line_graph)


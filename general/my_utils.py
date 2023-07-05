#
# Utility for Exploratory Data Analysis
#

import numpy as np
import pandas as pd
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

import ipywidgets as widgets
from ipywidgets import interact
import folium 
from colour import Color
from collections import defaultdict

from typing import List

# settings for plots
FONT_SIZE_TICKS = 12
FONT_SIZE_TITLE = 20
FONT_SIZE_AXES = 16

#
# create an hystohram for the data in a column in a DataFrame
#
def create_histogram_plot(df: pd.core.frame.DataFrame, bins: int):
    '''Creates an interactive histogram
    
    Args:
        df (pd.core.frame.DataFrame): The dataframe with the data.
        bins (int): number of bins for the histogram,
        column_name: the col chosen in the DataFrame
    
    '''
    def _interactive_histogram_plot(column_name):
        x = df[column_name].values 
        try:
            plt.figure(figsize=(12,6))
            plt.xlabel(f'{column_name}', fontsize=FONT_SIZE_AXES)
            plt.ylabel('Number of measurements', fontsize=FONT_SIZE_AXES)
            plt.hist(x, bins=bins)
            plt.title(f'Data: {column_name}', fontsize=FONT_SIZE_TITLE)
            plt.xticks(fontsize=FONT_SIZE_TICKS)
            plt.yticks(fontsize=FONT_SIZE_TICKS)
            
            # modified by LS
            plt.grid(True)
            plt.show()
        except ValueError:
            print('Histogram cannot be shown for selected values as there is no data')
    
    # Widget for picking the column
    col_selection = widgets.Dropdown(options=df.columns,
        description="Columns"
    )

    
    # Putting it all together
    interact(_interactive_histogram_plot, column_name=col_selection);
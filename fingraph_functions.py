## FinGraph -- fingraph_functions.py

# std lib imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

def query_yahoo_finance(ticker, start_date, end_date):
    """
    obtain a dataframe of price and volume data for given ticker
    from Yahoo Finance
    note: Yahoo Finance historical API has been deprecated
          fix_yahoo_finance contains a temporary fix
    """
    yf.pdr_override()
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    return data

def generate_title(data, ticker, price_type):
    """
    generate a title for the price / volume data subplot
    """
    title = ticker.upper() + " daily " + price_type.lower() + ": "
    title += str(data.index[0].date()) + " to " + str(data.index[-1].date())
    return title


def generate_plot(data, ticker, option):
    """
    generate a matplotlib plot for the price / volume data
    with optional second subplot for technical indicator
    """
    price_type = 'close' 

    if option == 'none':
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        title = generate_title(data, ticker, price_type)
        ax.set_title(title)
        data[price_type.title()].plot(ax=ax)

    plt.show()

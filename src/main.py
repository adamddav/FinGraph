## FinGraph -- main.py
## by Adam Davidson
## 2017

# std lib imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# project imports
import fingraph_functions as fgf

# request ticker and time frame inputs from user
ticker = input("Enter security ticker: ")
start_date = input("Enter the start date (yyyy-mm-dd): ")
end_date = input("Enter the end date (yyyy-mm-dd): ")

# request price type and optional keyword for second subplot
price_type = input("Select price data type\n\
        (Open, High, Low, Close, Adj Close, Volume): ")
option = input("Select optional secondary plot\n\
        (Stoch Osc, None): ")
if option.lower() == 'stoch osc':
    tune = input("Would you like to tune the Oscillator or use default settings?\n\
            (y or n): ")
    settings = []
    if tune.lower() == 'y':
        settings.append(int(input("Enter length of lookback window (default 14): ")))
        settings.append(int(input("Number of periods to slow %K (default 1): ")))
        settings.append(int(input("Number of periods for %D moving avg (default 3): ")))
        
# generate nessecary price /volume data
data = fgf.query_yahoo_finance(ticker.upper(), start_date, end_date)

# generate price /volume plot and optional subplot
fgf.generate_plot(data, ticker, price_type, option, settings)

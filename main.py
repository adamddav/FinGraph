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
start_date = input("Enter the start date (YY-mm-dd): ")
end_date = input("Enter the end date (YY-mm-dd): ")

# request price type and optional keyword for second subplot
price_type = input("Select price data type\n\
        (Open, High, Low, Close, Adj Close, Volume): ")
option = input("Select optional secondary plot\n\
        (Stoch Osc, None): ")

# generate nessecary price /volume data
data = fgf.query_yahoo_finance(ticker.upper(), start_date, end_date)

# generate price /volume plot and optional subplot
fgf.generate_plot(data, ticker, price_type, option)

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

data = fgf.query_yahoo_finance(ticker.upper(), start_date, end_date)

fgf.generate_plot(data, ticker, 'none')

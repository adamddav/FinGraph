## FinGraph -- main.py
## by Adam Davidson
## 2017

# project imports
import fingraph_functions as fgf

# request ticker and time frame inputs from user
ticker = input("\nEnter security ticker: ")
start_date = input("\nEnter the start date (yyyy-mm-dd): ")
end_date = input("\nEnter the end date (yyyy-mm-dd): ")

# request price type and optional keyword for second subplot
price_type = input("\nSelect price data type\n\
        (Open, High, Low, Close, Adj Close, Volume): ")
option = input("\nSelect optional secondary plot\n\
        (MACD, Stoch Osc, None): ")
settings = []

if option.lower() == 'macd':
    tune = input("\nWould you like to tune the MACD or use default settings?\n\
            (y or n): ")
    if tune.lower() == 'y':
        settings.append(int(input("\nNumber of days for fast EMA (default 12): ")))
        settings.append(int(input("\nNumber of days for slow EMA (default 26): ")))
        settings.append(int(input("\nNumber of days for signal EMA (default 9): ")))

if option.lower() == 'stoch osc':
    tune = input("\nWould you like to tune the Oscillator or use default settings?\n\
            (y or n): ")
    if tune.lower() == 'y':
        settings.append(int(input("\nEnter length of lookback window (default 14): ")))
        settings.append(int(input("\nNumber of periods to slow %K (default 3): ")))
        settings.append(int(input("\nNumber of periods for %D moving avg (default 3): ")))
        
# generate price / volume plot and optional subplot
try:
    fgf.generate_plot(ticker, start_date, end_date, price_type, option, settings)
except (KeyError, IndexError):
    print("Error retrieving data. Try again...\n")

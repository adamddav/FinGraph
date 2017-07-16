## FinGraph -- fingraph_functions.py

# std lib imports
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

# project imports
from fingraph_classes import StochasticOscillator, MACD

# select ggplot style for matplotlib
import matplotlib
matplotlib.style.use('ggplot')

def query_yahoo_finance(ticker, start_date, end_date):
    """
    obtain a dataframe of price and volume data for given ticker
    from Yahoo Finance
    note: Yahoo Finance historical API has been deprecated
          fix_yahoo_finance contains a temporary fix
    """
    yf.pdr_override()
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    print('\n')       # force command prompt onto new line
    return data

def generate_title(data, ticker, price_type):
    """
    generate a title for the price / volume data subplot
    """
    title = ticker.upper() + " daily " + price_type.lower() + ": "
    title += str(data.index[0].date()) + " to " + str(data.index[-1].date())
    return title


def generate_plot(ticker, start_date, end_date, price_type, option, settings):
    """
    generate a matplotlib plot for the price / volume data
    with optional second subplot for technical indicator
    """
    option = option.lower()
    if option == 'none':
        # generate nessecary price / volume data
        data = query_yahoo_finance(ticker, start_date, end_date)

        # create plot
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        title = generate_title(data, ticker, price_type)
        ax.set_title(title)
        data[price_type.title()].plot(ax=ax, color='k')

    elif option == 'stoch osc':
        # instantiate stoch osc object
        if not settings:
            osc = StochasticOscillator()
        else:
            osc = StochasticOscillator(*settings)
        
        # obtain adjusted start date and generate data
        new_start = osc.extend_start_date(start_date)
        data = query_yahoo_finance(ticker, new_start, end_date)
        data = osc.add_to_dataframe(data)
        data = data.ix[start_date:]

        # create plot
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,
                                        gridspec_kw=dict(height_ratios=[4, 1]))
        title1 = generate_title(data, ticker, price_type)
        ax1.set_title(title1)
        data[price_type.title()].plot(ax=ax1, color='k')

        ax2.set_ylim([-5, 105])
        data['Upper Band'].plot(ax=ax2, color='k')
        data['Middle Band'].plot(ax=ax2, color='k', linestyle='--')
        data['Lower Band'].plot(ax=ax2, color='k')
        data['%%K'].plot(ax=ax2, color='b')
        data['%%D'].plot(ax=ax2, color='r')

    elif option == 'macd':
        # instantiate macd object
        if not settings:
            macd = MACD()
        else:
            macd = MACD(*settings)

        # obtain adjusted start date and generate data
        new_start = macd.extend_start_date(start_date)
        data = query_yahoo_finance(ticker, new_start, end_date)
        data = macd.add_to_dataframe(data)
        data = data.ix[start_date:]

        # create plot
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,
                                        gridspec_kw=dict(height_ratios=[4, 1]))
        title1 = generate_title(data, ticker, price_type)
        ax1.set_title(title1)
        data[price_type.title()].plot(ax=ax1, color='k')

        upper_bound = max(0, data['MACD'].max()) + 0.5
        lower_bound = min(0, data['MACD'].min()) - 0.5
        ax2.set_ylim([lower_bound, upper_bound])
        data['Baseline'].plot(ax=ax2, color='k')
        data['MACD'].plot(ax=ax2, color='b')
        data['Signal'].plot(ax=ax2, color='r')
        ax2.bar(data.index, data['Divergence'])

    plt.show()
    return data

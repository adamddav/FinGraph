## FinGraph -- fingraph_classes.py

# std lib imports
import datetime as dt
import pandas as pd

class StochasticOscillator(object):
    """
    representation of a stochastic oscillator
    """
    def __init__(self, length=14, k_period=3, d_period=3,
                    upper_band=80, lower_band=20):
        """
        defaults represent a typical callibration
        """
        self.length = length
        self.k_period = k_period
        self.d_period = d_period
        self.upper_band = upper_band
        self.lower_band = lower_band

    def extend_start_date(self, start_date):
        """
        extends requested start date further into the past
        to accommodate moving window lags
        """
        old_start = dt.datetime.strptime(start_date, "%Y-%m-%d")
        lag_sum = self.length + self.k_period + self.d_period
        weekends = (lag_sum % 5) * 2
        start_adjust = lag_sum + weekends + 5
        new_start = old_start - dt.timedelta(days=start_adjust)
        return new_start.strftime("%Y-%m-%d")

    def add_to_dataframe(self, df):
        """
        add the stochastic oscillator data to a standard
        Yahoo Finance dataframe
        """
        df['High mw'] = df['Close'].rolling(window=self.length).max()
        df['Low mw'] = df['Close'].rolling(window=self.length).min()
        df['Fast %%K'] = 100 * (df['Close'] - df['Low mw']) / (df['High mw'] - df['Low mw'])
        df['%%K'] = df['Fast %%K'].rolling(window=self.k_period).mean()
        df['%%D'] = df['%%K'].rolling(window=self.d_period).mean()
        df['Upper Band'] = self.upper_band 
        df['Middle Band'] = 50
        df['Lower Band'] = self.lower_band 
        return df




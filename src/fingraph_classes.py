## FinGraph -- fingraph_classes.py

# std lib imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

    def add_to_dataframe(self, df):
        """
        add the stochastic oscillator data to a standard
        Yahoo Finance dataframe.
        """
        df['High'] = pd.rolling_max(df['Close'], self.length)
        df['Low'] = pd.rolling_min(df['Close'], self.length)
        df['Fast %%K'] = 100 * (df['Close'] - df['Low']) / (df['High'] - df['Low'])
        df['%%K'] = pd.rolling_mean(df['Fast %%K'], self.k_period)
        df['%%D'] = pd.rolling_mean(df['%%K'], self.d_period)
        df['Upper Band'] = self.upper_band 
        df['Middle Band'] = 50
        df['Lower Band'] = self.lower_band 
        return df




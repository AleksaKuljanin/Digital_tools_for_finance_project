import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath('../src/features'))
from variables import *


# ----- Calculate returns -----
def calculate_stock_returns(saving_path, period, file_suffix):
    df_stock_prices = pd.read_hdf(path_stock_prices, 'df')
    df_stock_prices_temp = df_stock_prices.ffill(axis=0)
    df_stock_returns = df_stock_prices_temp.pct_change(periods=period)
    df_stock_returns[df_stock_prices.isna()] = np.nan
    df_stock_returns.to_hdf(saving_path + file_suffix, key='df', mode='w')
    return df_stock_returns



# ----- Calculate signal & weights -----
# loop for different lookback periods
def signal_calculation(lookback_periods, number_of_positions, holding_period, long_only):
    last_lookback_period = lookback_periods[-1]
    for i, lookback in enumerate(lookback_periods):
        portfolio_performance(lookback, last_lookback_period, number_of_positions, holding_period, long_only)

# long only signal & weights
def stock_signal_calculation_long_only(row, n):
    binary_row = pd.Series(0, index=row.index)
    top_performers = row.nlargest(n).index
    binary_row = pd.Series(0.0, index=row.index)
    binary_row[top_performers] = 1.0 / n
    return binary_row

# long short signal & weights
def stock_signal_calculation_long_short(row, n: float):
    n_short = int(n // 2) # handle odd numbers
    n_long = n_short + n % 2
    binary_row = pd.Series(0.0, index=row.index)
    top_performers = row.nsmallest(n_long).index
    worst_performers = row.nlargest(n_short).index
    binary_row[top_performers] = 1.0 / n_long
    binary_row[worst_performers] = -1.0 / n_short
    return binary_row



# ----- Calculate portfolio performance -----
df_portfolio_performances = pd.DataFrame()
def portfolio_performance(lookback, last_lookback_period, number_of_positions, holding_period, long_only):
    file_suffix = "_" + str(lookback) + "M"
    df_stock_returns = calculate_stock_returns(path_stock_returns_holding_period, holding_period, "") # get returns for holding period
    df_stock_returns_signal = calculate_stock_returns(path_stock_returns_signal, lookback, file_suffix) # get returns for signal
    
    if long_only == False:
        # Long Short
        file_suffix_LS = "_long_short" + file_suffix
        df_weights_long_short = df_stock_returns_signal.iloc[2:].apply(lambda row: stock_signal_calculation_long_short(row, number_of_positions), axis=1)
        df_weights_long_short.to_hdf(path_stock_weights + file_suffix_LS, key='df', mode='w')
        df_aligned_weights_long_short = df_weights_long_short.shift(holding_period)
    
    # Long only
    file_suffix_L = "_long_only" + file_suffix
    df_weights_long_only = df_stock_returns_signal.iloc[2:].apply(lambda row: stock_signal_calculation_long_only(row, number_of_positions), axis=1)
    df_weights_long_only.to_hdf(path_stock_weights + file_suffix_L, key='df', mode='w')
    df_aligned_weights_long_only = df_weights_long_only.shift(holding_period)

    # Portfolio construction
    df_portfolio_performances[f'Lookback_{lookback}M'] = (df_aligned_weights_long_only * df_stock_returns).sum(axis=1)
    if lookback == last_lookback_period:
        df_portfolio_performances.to_hdf(path_portfolio_performances, key='df', mode='w')


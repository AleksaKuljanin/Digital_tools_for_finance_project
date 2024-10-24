import pandas as pd
import h5py

# Get raw data and save as h5 file
def get_data(source_path, saving_path):
    df_raw_data = pd.read_excel(source_path)
    df_raw_data.set_index('Date', inplace=True)
    df_raw_data.to_hdf(saving_path, key='df', mode='w')

# Calculate monthly stock returns 
def calculate_stock_returns(path, saving_path):
    df_stock_prices = pd.read_hdf(path, 'df')
    df_stock_returns = df_stock_prices.pct_change()
    df_stock_returns = df_stock_returns.dropna()
    df_stock_returns.to_hdf(saving_path, key='df', mode='w')

 
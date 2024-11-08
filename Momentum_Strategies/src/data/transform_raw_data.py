import pandas as pd
import h5py

# Get raw data and save as h5 file
def get_data(source_path, saving_path):
    df_raw_data = pd.read_excel(source_path)
    df_raw_data.set_index('Date', inplace=True)
    df_raw_data.to_hdf(saving_path, key='df', mode='w')

 
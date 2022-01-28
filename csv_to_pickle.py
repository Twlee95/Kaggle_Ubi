import numpy as np
import pandas as pd
import IPython.display as display

def transform_csv2pickle(path, usecols, dtype):
    train = pd.read_csv(
        path,
        usecols=usecols,
        dtype=dtypes
    )
    train.to_pickle(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.pkl")


path = r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.csv"

# basecols = ['row_id', 'time_id', 'investment_id', 'target']

basecols = ['time_id', 'investment_id', 'target']
features = [f'f_{i}' for i in range(300)]

dtypes = {
    'row_id': 'str',
    'time_id': 'float16',
    'investment_id': 'float16',
    'target': 'float16',
}
for col in features:
    dtypes[col] = 'float32'

transform_csv2pickle(path, basecols+features, dtypes)

train = pd.read_pickle(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.pkl")
display(train.info())
display(train.head())
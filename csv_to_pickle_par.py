import os
import pandas as pd
import numpy as np
import gc
import math

def reduce_memory_usage(df, features):
    for feature in features:
        item = df[feature].astype(np.float16)
        df[feature] = item
        del item
        gc.collect()

train = pd.read_csv(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.csv")
train.to_parquet(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.parquet")

n_features = 300
features = [f'f_{i}' for i in range(n_features)]
feature_columns = ['investment_id', 'time_id'] + features
train = pd.read_parquet(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.parquet", columns=feature_columns + ["target"])
train.head()

train.info()


reduce_memory_usage(train, features + ["target"])
train.info()
train.to_pickle(r"C:\Users\USER\Desktop\ubiquant-market-prediction\train.pkl")

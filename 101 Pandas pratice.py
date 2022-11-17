# 101 Pandas pratice.py

import pandas as pd
import numpy as np

df = pd.read_csv(filepath_or_buffer="./data_gero.csv")
# print(df)

print(df.loc[:])  # gives you an element by INDEX

print("-------------------------------")

print(df.iloc[-1])  # gives you an element by POSITION

print("-------------------------------")

print(df.describe())

print("-------------------------------")

import pandas as pd
import numpy as np

data = pd.read_csv("./comercio_barcelona_2019.csv")

data_head = data.head()
data_columns = data.columns
print("How many columns: ", len(data_columns))

# print(data_columns)

# for col in data_columns:
#     print(f"\t {col}")

print(data["Nom_Principal_Activitat"].unique())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_gero.csv")
plt.pie(df['name'], df[' salary'])
plt.xlabel('Name')
plt.xlabel('Salary')
plt.show()



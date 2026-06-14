import pandas as pd

df = pd.read_csv("topics.csv")

print(df.columns)
print(df.isnull().sum())

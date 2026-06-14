import pandas as pd

df = pd.read_csv(r"datasets\questions.csv")

print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal rows:", len(df))
import pandas as pd

df = pd.read_csv(r"datasets\questions.csv")

print("Subjects:")
print(df["Subject"].unique())

print("\nDifficulties:")
print(df["Difficulty"].unique())

print("\nMarks:")
print(df["Marks"].unique())
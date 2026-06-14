import pandas as pd

df = pd.read_csv(r"datasets\questions.csv")

# Remove repeated header rows
df = df[
    (df["Question"] != "Question") &
    (df["Marks"] != "Marks") &
    (df["Difficulty"] != "Difficulty") &
    (df["Subject"] != "Subject")
]

# Convert marks to integer
df["Marks"] = df["Marks"].astype(int)

df.to_csv(r"datasets\questions.csv", index=False)

print("Dataset cleaned successfully!")
print("Rows:", len(df))
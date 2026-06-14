import pandas as pd

df = pd.read_csv(r"datasets/questions.csv")

df["Marks"] = df["Marks"].astype(int)

two_marks = int(input("How many 2 mark questions? "))
ten_marks = int(input("How many 10 mark questions? "))

total_marks = (two_marks * 2) + (ten_marks * 10)

partA = df[df["Marks"] == 2].sample(two_marks)
partB = df[df["Marks"] == 10].sample(ten_marks)

print("\n")
print(" " * 45 + f"TOTAL MARKS : {total_marks}")
print("\nQUESTION PAPER")
print("-" * 60)

print("\nPART - A (2 Marks Each)\n")

for i, (_, row) in enumerate(partA.iterrows(), 1):
    print(f"{i}. {row['Question']} ({row['Subject']})")

print(f"\n{two_marks} x 2 = {two_marks*2} Marks")

print("\n" + "-" * 60)

print("\nPART - B (10 Marks Each)\n")

for i, (_, row) in enumerate(partB.iterrows(), len(partA)+1):
    print(f"{i}. {row['Question']} ({row['Subject']})")

print(f"\n{ten_marks} x 10 = {ten_marks*10} Marks")

print("\n" + "-" * 60)

print(f"\nTOTAL = {total_marks} MARKS")
import pandas as pd
import random

df = pd.read_csv(r"datasets\questions.csv")

print("=== BLUEPRINT QUESTION PAPER GENERATOR ===")

ai_count = int(input("AI Questions: "))
ml_count = int(input("ML Questions: "))
os_count = int(input("OS Questions: "))
cn_count = int(input("CN Questions: "))
se_count = int(input("SE Questions: "))

paper = []

subjects = {
    "AI": ai_count,
    "ML": ml_count,
    "OS": os_count,
    "CN": cn_count,
    "SE": se_count
}

for subject, count in subjects.items():

    rows = df[
        (df["Subject"] == subject) &
        (df["Marks"] == 10)
    ]

    if len(rows) >= count:
        selected = rows.sample(count)

        for _, row in selected.iterrows():
            paper.append(row)

print("\nQUESTION PAPER")
print("-" * 60)

total_marks = 0

for i, q in enumerate(paper, start=1):

    print(
        f"{i}. {q['Question']} ({q['Subject']})"
    )

    total_marks += int(q["Marks"])

print("\nTOTAL MARKS =", total_marks)
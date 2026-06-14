import pandas as pd

df = pd.read_csv(r"datasets/questions.csv")
df["Marks"] = df["Marks"].astype(int)

paper = []
qno = 1

while True:

    subject = input("\nSubject (AI/ML/OS/CN/SE or DONE): ").upper()

    if subject == "DONE":
        break

    difficulty = input("Difficulty (Easy/Medium/Hard): ").capitalize()

    marks = int(input("Marks (2 or 10): "))

    count = int(input("Number of Questions: "))

    questions = df[
        (df["Subject"] == subject) &
        (df["Difficulty"] == difficulty) &
        (df["Marks"] == marks)
    ]

    selected = questions.sample(
        min(count, len(questions))
    )

    for _, row in selected.iterrows():

        paper.append({
            "No": qno,
            "Question": row["Question"],
            "Subject": row["Subject"],
            "Marks": row["Marks"]
        })

        qno += 1


print("\n\nQUESTION PAPER")
print("="*60)

total = 0

for q in paper:

    print(
        f"{q['No']}. {q['Question']} ({q['Subject']}) [{q['Marks']} Marks]"
    )

    total += q["Marks"]

print("\nTotal Marks =", total)
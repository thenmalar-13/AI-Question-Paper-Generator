import pandas as pd

df = pd.read_csv(r"datasets\questions.csv")

print("=== AI QUESTION PAPER GENERATOR ===")

subject = input("Subject (AI/ML/OS/CN/SE): ")
difficulty = input("Difficulty (Easy/Medium/Hard): ")
marks = int(input("Marks (2 or 10): "))
count = int(input("Number of Questions: "))

filtered = df[
    (df["Subject"] == subject) &
    (df["Difficulty"] == difficulty) &
    (df["Marks"] == marks)
]

if len(filtered) == 0:
    print("No questions found")
else:
    questions = filtered.sample(min(count, len(filtered)))

    print("\nGenerated Question Paper:\n")

    for i, row in enumerate(questions["Question"], 1):
        print(f"{i}. {row}")
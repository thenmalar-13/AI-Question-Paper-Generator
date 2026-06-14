import random

question_starters = {
    "Easy": [
        "Define",
        "What is",
        "List",
        "Name"
    ],

    "Medium": [
        "Explain",
        "Describe",
        "Differentiate",
        "Discuss"
    ],

    "Hard": [
        "Compare",
        "Evaluate",
        "Analyze",
        "Justify"
    ]
}

def generate_questions(topic, difficulty, num):

    questions = []

    for i in range(num):

        starter = random.choice(
            question_starters[difficulty]
        )

        questions.append(
            f"{starter} {topic}."
        )

    return questions


topic = input("Topic: ")
difficulty = input("Difficulty: ")
num = int(input("No of Questions: "))

generated = generate_questions(
    topic,
    difficulty,
    num
)

print("\nGenerated Questions:\n")

for i, q in enumerate(generated, 1):
    print(f"{i}. {q}")
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model(
    "models/question_generator.keras"
)

with open(
    "models/tokenizer_generator.pkl",
    "rb"
) as f:
    tokenizer = pickle.load(f)

max_len = 12


def generate_question(subject, marks):

    seed_text = f"{subject} {marks}"

    for _ in range(10):

        token_list = tokenizer.texts_to_sequences(
            [seed_text]
        )[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_len-1,
            padding="pre"
        )

        prediction = model.predict(
            token_list,
            verbose=0
        )[0]

        predicted = np.random.choice(
            len(prediction),
            p=prediction
        )

        output = ""

        for word, index in tokenizer.word_index.items():

            if index == predicted:
                output = word
                break

        seed_text += " " + output

    return seed_text


def generate_multiple(subject, marks, count):

    questions = []

    for _ in range(count):

        questions.append(
            generate_question(subject, marks)
        )

    return questions
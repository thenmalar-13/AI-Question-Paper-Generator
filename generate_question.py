import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("models/question_generator.keras")

with open("models/tokenizer_generator.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_sequence_len = 8


def generate(seed_text, next_words=5):

    for _ in range(next_words):

        token_list = tokenizer.texts_to_sequences(
            [seed_text]
        )[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_sequence_len - 1,
            padding='pre'
        )

        predicted = np.argmax(
            model.predict(token_list, verbose=0),
            axis=-1
        )[0]

        output_word = ""

        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break

        seed_text += " " + output_word

    return seed_text


while True:

    topic = input("Enter Topic: ")

    print(
        generate(topic.lower(), 5)
    )
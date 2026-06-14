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

max_len = 8


def generate(seed_text):

    for _ in range(5):

        token_list = tokenizer.texts_to_sequences(
            [seed_text]
        )[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_len-1,
            padding="pre"
        )

        predicted = np.argmax(
            model.predict(
                token_list,
                verbose=0
            ),
            axis=-1
        )[0]

        output = ""

        for word, index in tokenizer.word_index.items():

            if index == predicted:
                output = word
                break

        seed_text += " " + output

    return seed_text


topic = input("Enter Topic: ")

print(
    "\nGenerated Question:"
)

print(
    generate(topic.lower())
)
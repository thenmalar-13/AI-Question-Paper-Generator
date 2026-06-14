import pandas as pd
import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

data = pd.read_csv("datasets/questions.csv")
texts = data["Question"].astype(str)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

total_words = len(tokenizer.word_index) + 1

input_sequences = []

for line in texts:

    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):

        n_gram = token_list[:i+1]

        input_sequences.append(n_gram)

max_len = max(len(x) for x in input_sequences)

input_sequences = np.array(
    pad_sequences(
        input_sequences,
        maxlen=max_len,
        padding="pre"
    )
)

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

model = Sequential([
    Embedding(total_words, 64),
    LSTM(100),
    Dense(total_words, activation="softmax")
])

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.fit(
    X,
    y,
    epochs=100
)

model.save("models/question_generator.keras")

with open(
    "models/tokenizer_generator.pkl",
    "wb"
) as f:

    pickle.dump(tokenizer, f)

print("Generator Model Saved!")
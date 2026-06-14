import pandas as pd
import numpy as np
import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.utils import to_categorical

# Load dataset
data = pd.read_csv("datasets/questions.csv")

questions = data["Question"].astype(str)

# Convert all questions into one text corpus
corpus = []

for q in questions:
    corpus.append(q.lower())

# Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)

total_words = len(tokenizer.word_index) + 1

input_sequences = []

for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        ngram_sequence = token_list[:i+1]
        input_sequences.append(ngram_sequence)

# Padding
max_sequence_len = max([len(x) for x in input_sequences])

input_sequences = np.array(
    pad_sequences(
        input_sequences,
        maxlen=max_sequence_len,
        padding='pre'
    )
)

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

y = to_categorical(y, num_classes=total_words)

# LSTM Model
model = Sequential()

model.add(
    Embedding(
        total_words,
        100,
        input_length=max_sequence_len - 1
    )
)

model.add(
    LSTM(150)
)

model.add(
    Dense(total_words, activation='softmax')
)

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(
    X,
    y,
    epochs=100,
    verbose=1
)

model.save("models/question_generator.keras")

with open("models/tokenizer_generator.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Generator Model Saved!")
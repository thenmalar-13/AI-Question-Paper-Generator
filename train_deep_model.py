import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load dataset
data = pd.read_csv("datasets/questions.csv")

data = data.dropna()

questions = data["Question"].astype(str)

difficulty = data["Difficulty"]

# Encode labels
encoder = LabelEncoder()

labels = encoder.fit_transform(difficulty)

# Convert text to numbers
tokenizer = Tokenizer(num_words=5000)

tokenizer.fit_on_texts(questions)

sequences = tokenizer.texts_to_sequences(questions)

X = pad_sequences(sequences, maxlen=20)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.2,
    random_state=42
)

# Neural Network
model = Sequential()

model.add(Dense(128, activation="relu", input_shape=(20,)))

model.add(Dropout(0.3))

model.add(Dense(64, activation="relu"))

model.add(Dense(3, activation="softmax"))

# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=16,
    validation_data=(X_test, y_test)
)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)

print("Accuracy:", accuracy)

# Save
model.save("models/deep_model.keras")

with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

with open("models/label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Model Saved Successfully")
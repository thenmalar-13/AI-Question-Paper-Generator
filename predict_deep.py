import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("models/deep_model.keras")

with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("models/label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

while True:

    q = input("Enter Question: ")

    seq = tokenizer.texts_to_sequences([q])

    padded = pad_sequences(seq, maxlen=20)

    prediction = model.predict(padded)

    label = np.argmax(prediction)

    print(
        "Difficulty:",
        encoder.inverse_transform([label])[0]
    )
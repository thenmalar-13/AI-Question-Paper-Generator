import pickle

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

while True:

    question = input("Enter question: ")

    q = vectorizer.transform([question])

    prediction = model.predict(q)

    print("Difficulty:", prediction[0])
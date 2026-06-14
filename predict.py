import joblib

difficulty_model = joblib.load("difficulty_model.pkl")
subject_model = joblib.load("subject_model.pkl")
marks_model = joblib.load("marks_model.pkl")
topic_model = joblib.load("topic_model.pkl")

question = input("Enter Question: ")

print("\nPredictions")
print("Difficulty :", difficulty_model.predict([question])[0])
print("Subject :", subject_model.predict([question])[0])
print("Marks :", marks_model.predict([question])[0])
print("Topic :", topic_model.predict([question])[0])
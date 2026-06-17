# train_classifier.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv(r"datasets\questions.csv")
X = data["Question"]

targets = {
    "difficulty": data["Difficulty"],
    "subject": data["Subject"],
    "marks": data["Marks"],
    "topic": data["Topic"]
}

for name, y in targets.items():

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print(f"{name} accuracy = {acc:.2f}")

    joblib.dump(model, f"{name}_model.pkl")
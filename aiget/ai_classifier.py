from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

model_path = "aiget/model.joblib"

# For demo, training a basic model
TRAIN = True
if TRAIN or not os.path.exists(model_path):
    X_train = ["fix bug", "add feature", "refactor code"]
    y_train = ["bug", "feature", "refactor"]

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X_train)

    clf = LogisticRegression().fit(X_vec, y_train)
    joblib.dump((clf, vectorizer), model_path)
else:
    clf, vectorizer = joblib.load(model_path)

def classify_todo(text):
    vec = vectorizer.transform([text])
    return clf.predict(vec)[0]

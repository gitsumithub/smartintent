import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv('data/utterances.csv')

X = df['utterance']
y = df['intent']

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=200))
])

pipeline.fit(X, y)
joblib.dump(pipeline, 'model/classifier.pkl')

print("✅ Model trained and saved to model/classifier.pkl")

# confusion_test.py

import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix

df = pd.read_csv("dataset/features.csv")

X = df.drop("label", axis=1)
y = df["label"]

model = joblib.load("url_model.pkl")

pred = model.predict(X)

print(confusion_matrix(y, pred))

print("Unique predictions:", set(pred))
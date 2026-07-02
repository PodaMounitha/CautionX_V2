import joblib

model = joblib.load("url_model.pkl")

print("Model Type:", type(model).__name__)
print("Trees:", len(model.estimators_))
print("Classes:", model.classes_)
print("Features:", model.feature_names_in_)
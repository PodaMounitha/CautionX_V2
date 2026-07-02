import pandas as pd
from feature_extraction import extract_features

df = pd.read_csv("dataset/cleaned_malicious_phish.csv")

feature_rows = []

for _, row in df.iterrows():

    features = extract_features(row['url'])

    features['label'] = row['label']

    feature_rows.append(features)

feature_df = pd.DataFrame(feature_rows)

print(feature_df.head())

feature_df.to_csv(
    "dataset/features.csv",
    index=False
)

print("Feature dataset saved.")
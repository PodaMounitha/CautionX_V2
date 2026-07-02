import pandas as pd

df = pd.read_csv("dataset/malicious_phish.csv")

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nNull Values:")
print(df.isnull().sum())
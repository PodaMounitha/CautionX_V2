import pandas as pd

df = pd.read_csv("dataset/malicious_phish.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove nulls
df.dropna(inplace=True)

# Convert to binary classification
df['label'] = df['type'].apply(
    lambda x: 0 if x.lower() == 'benign' else 1
)

print("\nAfter Cleaning:", df.shape)

print("\nClass Distribution:")
print(df['label'].value_counts())

df.to_csv("dataset/cleaned_malicious_phish.csv", index=False)

print("\nSaved cleaned_malicious_phish.csv")
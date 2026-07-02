# # # import pandas as pd

# # # df = pd.read_csv("dataset/cleaned_malicious_phish.csv")

# # # print(df["label"].value_counts())

# # # import pandas as pd

# # # df = pd.read_csv("dataset/features.csv")

# # # print(df.columns.tolist())

# # # from feature_extraction import extract_features

# # # features = extract_features("google.com")

# # # print(list(features.keys()))
# # # print(features)

# # # test_prediction.py

# # # import joblib
# # # from feature_extraction import extract_features

# # # model = joblib.load("url_model.pkl")

# # # urls = [
# # #     "google.com",
# # #     "github.com",
# # #     "openai.com",
# # #     "paypal-login-security.net"
# # # ]

# # # for url in urls:

# # #     features = extract_features(url)

# # #     pred = model.predict(
# # #         [list(features.values())]
# # #     )[0]

# # #     confidence = max(
# # #         model.predict_proba(
# # #             [list(features.values())]
# # #         )[0]
# # #     )

# # #     print("\nURL:", url)
# # #     print("Prediction:", pred)
# # #     print("Confidence:", confidence)

# # # import pandas as pd

# # # df = pd.read_csv("dataset/features.csv")

# # # print(df.head())
# # # print(df.columns)


# # import pandas as pd

# # df = pd.read_csv("dataset/features.csv")

# # print(df['label'].value_counts())

# # print()

# # print(df.groupby('label').mean())

# import pandas as pd
# import joblib
# from feature_extraction import extract_features

# model = joblib.load("url_model.pkl")

# urls = [
#     "https://www.google.com/search?q=test",
#     "https://github.com/openai/chatgpt",
#     "https://www.wikipedia.org/wiki/India",
#     "http://paypal-login-security.net/login"
# ]

# for url in urls:
#     X = pd.DataFrame([extract_features(url)])
#     print(url)
#     print(model.predict(X)[0])
#     print(model.predict_proba(X)[0])
#     print()

import pandas as pd

df = pd.read_csv("dataset/cleaned_malicious_phish.csv")

print(df["type"].value_counts())
print(df.head(20))
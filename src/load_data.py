import pandas as pd


df = pd.read_csv("application_train.csv", encoding="ISO-8859-1")
print(df.head())
print(df.shape)
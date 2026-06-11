import pandas as pd

df = pd.read_csv("application_train.csv", encoding="ISO-8859-1")

df=df.drop_duplicates()

df=df.isnull().sum()


print(df.sort_values(ascending=False).head())
df.fillna(df.median(numeric_only=True), inplace=True)
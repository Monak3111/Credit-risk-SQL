import pandas as pd

df = pd.read_csv("application_train.csv", encoding="ISO-8859-1")

df.columns

df["DEBT_INCOME_RATIO"] = (
    df["AMT_CREDIT"] /
    df["AMT_INCOME_TOTAL"]
)

df["ANNUITY_INCOME_RATIO"] = (
    df["AMT_ANNUITY"] /
    df["AMT_INCOME_TOTAL"]
)

df["CREDIT_GOODS_RATIO"] = (
    df["AMT_CREDIT"] /
    df["AMT_GOODS_PRICE"]
)
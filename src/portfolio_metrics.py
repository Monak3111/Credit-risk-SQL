import pandas as pd
df = pd.read_csv("application_train.csv", encoding="ISO-8859-1")


-----------------------------
df["DEBT_INCOME_RATIO"] = df["AMT_CREDIT"] / (df["AMT_INCOME_TOTAL"] + 1)
df["ANNUITY_INCOME_RATIO"] = df["AMT_ANNUITY"] / (df["AMT_INCOME_TOTAL"] + 1)
df["CREDIT_GOODS_RATIO"] = df["AMT_CREDIT"] / (df["AMT_GOODS_PRICE"] + 1)


df["risk_score"] = (
    0.4 * df["DEBT_INCOME_RATIO"] +
    0.3 * df["ANNUITY_INCOME_RATIO"] +
    0.2 * df["DAYS_BIRTH"].abs() / 10000 +
    0.1 * df["EXT_SOURCE_2"].fillna(0)
)

# normalize between 0 and 1
df["risk_score"] = (
    df["risk_score"] - df["risk_score"].min()
) / (
    df["risk_score"].max() - df["risk_score"].min()
)





portfolio_default_rate = df["TARGET"].mean()

average_risk_score = df["risk_score"].mean()

high_risk_customers = df[df["risk_score"] > 0.7].shape[0]

loan_exposure = df["AMT_CREDIT"].sum()

df["expected_loss"] = df["risk_score"] * df["AMT_CREDIT"]
expected_loss = df["expected_loss"].sum()

print("Portfolio Default Rate:", portfolio_default_rate)
print("Average Risk Score:", average_risk_score)
print("High Risk Customers:", high_risk_customers)
print("Loan Exposure:", loan_exposure)
print("Expected Loss:", expected_loss)

import matplotlib.pyplot as plt
fig = px.histogram(
    df,
    x="AMT_CREDIT",
    color="TARGET"
)

st.plotly_chart(fig)
import joblib
import pandas as pd

model = joblib.load(
    "credit_risk_model.pkl"
)

sample = pd.DataFrame({
    "AMT_INCOME_TOTAL":[250000],
    "AMT_CREDIT":[500000],
    "AMT_ANNUITY":[25000]
})

prob = model.predict_proba(sample)

print(prob)



def risk_category(prob):

    if prob < 0.30:
        return "LOW"

    elif prob < 0.60:
        return "MEDIUM"

    else:
        return "HIGH"

        print(risk_category)
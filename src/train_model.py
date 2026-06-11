import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("application_train.csv", encoding="ISO-8859-1")

features = [
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY"
]

X = df[features]

y = df["TARGET"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))

import joblib


joblib.dump(
    model,
    "credit_risk_model.pkl"
)
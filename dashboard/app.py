import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Credit Risk Scoring",
    layout="wide"
)

st.title("🏦 Credit Risk Scoring Dashboard")

model = joblib.load(
    "credit_risk_model.pkl"
)

income = st.sidebar.number_input(
    "Income",
    value=250000
)

credit = st.sidebar.number_input(
    "Credit Amount",
    value=500000
)

annuity = st.sidebar.number_input(
    "Annuity",
    value=25000
)

input_df = pd.DataFrame({
    "AMT_INCOME_TOTAL":[income],
    "AMT_CREDIT":[credit],
    "AMT_ANNUITY":[annuity]
})

prob = model.predict_proba(input_df)[0][1]

st.metric(
    "Default Probability",
    f"{prob:.2%}"
)

if prob < 0.3:
    st.success("LOW RISK")

elif prob < 0.6:
    st.warning("MEDIUM RISK")

else:
    st.error("HIGH RISK")
import streamlit as st
import pandas as pd
import joblib
import shap
from src.scoring import calculate_credit_score, loan_decision
from src.preprocessing_pipeline import preprocess_input
from src.explanation import generate_explanation

# LOAD MODEL
model = joblib.load("bin/models/final-model.pkl")

# SHAP EXPLAINER
explainer = shap.TreeExplainer(model)

# UI TITLE
st.title("💳 Credit Risk Prediction System")

st.write("Enter customer details to predict default risk")

# USER INPUTS
LIMIT_BAL = st.number_input("Credit Limit", min_value=0)

AGE = st.number_input("Age", min_value=18, max_value=100)

TOTAL_BILL = st.number_input("Total Bill Amount", min_value=0)

PAY_0 = st.slider("Recent Payment Status (PAY_0)", -2, 8, 0)
PAY_2 = st.slider("Payment Status (PAY_2)", -2, 8, 0)
PAY_3 = st.slider("Payment Status (PAY_3)", -2, 8, 0)

TOTAL_PAY = st.number_input("Total Payment Amount", min_value=0)

# PREDICT BUTTON
if st.button("Predict"):

    # Create DataFrame
    input_data = preprocess_input(
    LIMIT_BAL, AGE, PAY_0, PAY_2, PAY_3, TOTAL_BILL, TOTAL_PAY
    )

    # Generate SHAP values
    shap_values = explainer.shap_values(input_data)

    explanations = generate_explanation(
        shap_values,
        input_data,
        input_data.columns
    )

    st.subheader("🧠 Explanation")
    for exp in explanations:
        st.write("•", exp)
    
    # Prediction
    prob = model.predict_proba(input_data)[0][1]
    score = calculate_credit_score(prob)
    decision = loan_decision(score)

    # OUTPUT
    st.subheader("📊 Results")

    st.write(f"**Default Probability:** {prob:.2f}")
    st.write(f"**Credit Score:** {score}")
    st.write(f"**Loan Decision:** {decision}")

    # Color feedback
    if decision == "Approve":
        st.success("✅ Loan Approved")
    elif decision == "Review":
        st.warning("⚠️ Needs Review")
    else:
        st.error("❌ Loan Rejected")

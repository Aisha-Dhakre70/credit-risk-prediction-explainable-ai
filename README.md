# Credit Risk Prediction System with Explainable AI

An end-to-end machine learning system that predicts loan default risk using financial behavior data. The project integrates a credit scoring mechanism, threshold-based decisioning, and Explainable AI (SHAP) to provide interpretable predictions through a Streamlit web application.

> Designed to simulate real-world credit risk assessment used by financial institutions.

---

## Problem Statement

Financial institutions face significant challenges in assessing the risk of loan defaults. Incorrect approvals can lead to financial losses, while overly strict rejection policies can reduce business opportunities.

The objective of this project is to develop a machine learning-based system that predicts the likelihood of a customer defaulting on a loan using financial behavior data. The system aims to assist in decision-making by providing a risk score, loan approval recommendation, and interpretable explanations for each prediction.

---

## Objectives

* Predict probability of loan default using machine learning
* Handle imbalanced data using SMOTE
* Optimize model for detecting high-risk customers
* Provide interpretable predictions using SHAP
* Develop a user-friendly interface for decision support

---

## Features

* Predicts probability of loan default
* Custom credit scoring system
* Threshold-based decision: Approve / Review / Reject
* Explainable AI using SHAP (text-based explanations)
* Handles class imbalance using SMOTE
* Interactive Streamlit web application
* Clean and minimal user input interface

---

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* SHAP (Explainable AI)
* Streamlit

---

## Model Highlights

* ROC-AUC: ~0.74 (good discriminative performance)
* Optimized for recall of default cases (~65%)
* Uses SMOTE to handle class imbalance
* Threshold tuning applied for business-oriented decisions

> Note: The model prioritizes identifying high-risk customers (defaulters), even at the cost of lower overall accuracy, which aligns with real-world credit risk strategies.

---

## Input Features

The model uses key financial behavior features:

* Credit Limit (LIMIT_BAL)
* Total Repayment Amount (TOTAL_PAY)
* Recent Payment History (PAY_0, PAY_2, PAY_3)
* Toal Bill Amount (TOTAL_BILL)
* Age

---

## Output

* Default Probability
* Credit Score
* Loan Decision (Approve / Review / Reject)
* Top contributing factors (text-based explanation)

---

## Explainable AI

SHAP (SHapley Additive Explanations) is used to interpret model predictions.

Instead of visual plots, the system converts SHAP values into human-readable explanations such as:

* “Recent payment delay increases the risk of default”
* “Higher repayment amount reduces default risk”

This makes the model more transparent and user-friendly.

---

## Limitations

* The model may capture some bias from training data.
* Age has low direct correlation but contributes through feature interactions.
* The dataset is a benchmark dataset and may not fully represent real-world diversity.
* Model performance depends on the quality of input data.

---

## Future Improvements

* Add database integration to store user history
* Improve fairness by reducing potential bias
* Incorporate additional financial features
* Deploy as a cloud-based application
* Add real-time data integration

---

## Project Structure

```
credit-risk-project/
│
├── data/
├── bin/
│   ├── models/
├── notebooks/
│   ├── inspection_and_preprocessing.ipnyb
│   ├── feature_selection.ipnyb
│   ├── model.ipnyb
│   ├── explainability.ipnyb
├── src/
│   ├── preprocessing_pipeling.py
│   ├── scoring.py
│   ├── explainability.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Screenshots

<img width="838" height="875" alt="image" src="https://github.com/user-attachments/assets/07464de7-171a-4021-90ec-3ce15d819227" />


<img width="920" height="508" alt="image" src="https://github.com/user-attachments/assets/ece30844-7c97-4401-97cd-39db4f3438d5" />

---

## Key Learning Outcomes

* Handling imbalanced datasets using SMOTE
* Threshold tuning for business-focused optimization
* Building an end-to-end ML pipeline
* Implementing Explainable AI (SHAP)
* Deploying ML models using Streamlit
* Debugging real-world issues like feature mismatch

---

## Why This Project Matters

This project demonstrates how machine learning can support financial decision-making by balancing risk detection with interpretability. It reflects real-world challenges such as imbalanced data, trade-offs between accuracy and recall, and the need for transparent AI systems.

---
## Conclusion

This project demonstrates a practical approach to credit risk modeling by combining machine learning with explainability and business logic. It highlights the importance of balancing model performance with interpretability and real-world applicability.

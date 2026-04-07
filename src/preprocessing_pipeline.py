import joblib
import pandas as pd

# LOAD SCALER
scaler = joblib.load("C:/Users/User/OneDrive/Desktop/Semester - 8/credit-risk-project/bin/scaler.pkl")

def preprocess_input(LIMIT_BAL, AGE, PAY_0, PAY_2, PAY_3, TOTAL_BILL, TOTAL_PAY):

    data = {
        'LIMIT_BAL': LIMIT_BAL,
        'AGE': AGE,
        'PAY_0': PAY_0,
        'PAY_2': PAY_2,
        'PAY_3': PAY_3,
        'TOTAL_PAY': TOTAL_PAY,
        'TOTAL_BILL': TOTAL_BILL,
    }

    df = pd.DataFrame([data])

    # Apply scaling
    df[['LIMIT_BAL', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'TOTAL_PAY', 'TOTAL_BILL']] = \
        scaler.transform(df[['LIMIT_BAL', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'TOTAL_PAY', 'TOTAL_BILL']])

    expected_columns = [
    'LIMIT_BAL', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3',
    'TOTAL_BILL', 'TOTAL_PAY'
    ]

    df = df.reindex(columns=expected_columns)

    return df
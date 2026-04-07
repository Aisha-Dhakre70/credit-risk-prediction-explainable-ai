feature_map = {
    "PAY_0": "Recent payment delay",
    "PAY_2": "Past payment delay",
    "PAY_3": "Older payment delay",
    "LIMIT_BAL": "Credit limit",
    "TOTAL_PAY": "Total repayment amount",
    "TOTAL_BILL": "Total bill amount",
    "AGE": "Age"
}

def generate_explanation(shap_values, input_data, feature_names):
    explanation = []

    # Get values for single prediction
    shap_vals = shap_values[0]

    # Create list of (feature, value)
    feature_impact = list(zip(feature_names, shap_vals))

    # Sort by impact magnitude
    feature_impact = sorted(feature_impact, key=lambda x: abs(x[1]), reverse=True)

    # Take top 3 features
    for feature, impact in feature_impact[:3]:
        
        name = feature_map.get(feature, feature)
        
        if impact > 0:
            explanation.append(f"{name} increases the risk of default")
        else:
            explanation.append(f"{name} decreases the risk of default")

    return explanation
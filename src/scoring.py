"""
Probability	Score	Meaning
0.1     	~795	Low risk
0.5	        ~575	Medium risk
0.9	        ~355	High risk
"""


# Convert probability of default into credit score (300–850 scale)
def calculate_credit_score(prob):
    score = 850 - (550 * prob)
    return int(score)

def loan_decision(score):
    if score > 750:
        return "Approve"
    elif score > 600:
        return "Review"
    else:
        return "Reject"

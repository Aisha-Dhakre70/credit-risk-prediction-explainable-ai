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

"""
credit score ranging from 300 to 850. This transformation allows easier understanding of risk levels. Based on the score, a decision
system was implemented to categorize loan applications into approval, review, or rejection, making the system more practical and
user-friendly.
"""
import pandas as pd
from predict import predict_depression

# Same answers you tested
answers = {
    "phq1": 2,
    "phq2": 1,
    "phq3": 3,
    "phq4": 1,
    "phq5": 2,
    "phq6": 1,
    "phq7": 0,
    "phq8": 1,
    "phq9": 0
}

total = sum(answers.values())

print("Total Score:", total)

# Official PHQ-9 classification
if total <= 4:
    expected = "Minimal"
elif total <= 9:
    expected = "Mild"
elif total <= 14:
    expected = "Moderate"
elif total <= 19:
    expected = "Moderately Severe"
else:
    expected = "Severe"

print("Expected:", expected)

prediction = predict_depression(*answers.values())

print("Model Prediction:", prediction)
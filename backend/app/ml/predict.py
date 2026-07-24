import joblib
import pandas as pd
import os

# Get current folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model
model = joblib.load(
    os.path.join(BASE_DIR, "depression_model.pkl")
)

# Load label encoder
label_encoder = joblib.load(
    os.path.join(BASE_DIR, "label_encoder.pkl")
)


def predict_depression(
    phq1,
    phq2,
    phq3,
    phq4,
    phq5,
    phq6,
    phq7,
    phq8,
    phq9,
):
    """
    Predict depression level using trained Random Forest model.
    """

    data = pd.DataFrame(
        [[
            phq1,
            phq2,
            phq3,
            phq4,
            phq5,
            phq6,
            phq7,
            phq8,
            phq9
        ]],
        columns=[
            "phq1",
            "phq2",
            "phq3",
            "phq4",
            "phq5",
            "phq6",
            "phq7",
            "phq8",
            "phq9",
        ]
    )

    prediction = model.predict(data)

    depression_level = label_encoder.inverse_transform(
        prediction
    )[0]

    return depression_level
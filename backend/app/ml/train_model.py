import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("clean_dataset.csv")

# Features
X = df[
    [
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
]

# Target
y = df["depression_level"]

# -----------------------------------
# Encode Labels
# -----------------------------------

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

# -----------------------------------
# Train-Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

# -----------------------------------
# Train Random Forest
# -----------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------------
# Prediction
# -----------------------------------

y_pred = model.predict(X_test)

# -----------------------------------
# Evaluation
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("=" * 60)
print("Random Forest Model")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, y_pred))

# -----------------------------------
# Save Model
# -----------------------------------

joblib.dump(model, "depression_model.pkl")

joblib.dump(label_encoder, "label_encoder.pkl")

print("\n")
print("=" * 60)
print("Model Saved Successfully")
print("depression_model.pkl")
print("label_encoder.pkl")
print("=" * 60)
import pandas as pd


# Load dataset
df = pd.read_csv("dataset.csv")


# Keep only PHQ-9 columns
phq_columns = [
    "phq1",
    "phq2",
    "phq3",
    "phq4",
    "phq5",
    "phq6",
    "phq7",
    "phq8",
    "phq9"
]

df = df[phq_columns]


# Remove rows having missing values
df = df.dropna()


# Convert PHQ values to integers
for column in phq_columns:
    df[column] = df[column].astype(int)


# Calculate total PHQ-9 score
df["total_score"] = df[phq_columns].sum(axis=1)


# Function to assign depression level
def get_depression_level(score):

    if score <= 4:
        return "Minimal"

    elif score <= 9:
        return "Mild"

    elif score <= 14:
        return "Moderate"

    elif score <= 19:
        return "Moderately Severe"

    else:
        return "Severe"


# Create target column
df["depression_level"] = df["total_score"].apply(get_depression_level)


# Save cleaned dataset
df.to_csv("clean_dataset.csv", index=False)


print("=" * 50)
print("Dataset preprocessing completed successfully.")
print("=" * 50)
print(f"Total Records : {len(df)}")
print(df.head())
print("=" * 50)
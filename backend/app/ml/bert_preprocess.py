import pandas as pd

# Load dataset
df = pd.read_csv("reddit_dataset.csv")

# Remove unwanted column if present
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Combine title and text
df["text"] = (
    df["title"].fillna("") + " " +
    df["text"].fillna("")
)

# Keep only required columns
df = df[["text", "target"]]

# Remove duplicate posts
df = df.drop_duplicates()

# Remove empty rows
df = df.dropna()

# Save cleaned dataset
df.to_csv("reddit_clean.csv", index=False)

print("=" * 50)
print("Reddit Dataset Cleaned Successfully")
print("=" * 50)
print(df.head())
print()
print(df.shape)
print("=" * 50)
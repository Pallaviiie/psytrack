import pandas as pd

# Load dataset
df = pd.read_csv("reddit_dataset.csv")

print("=" * 50)
print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nTarget Distribution")
print(df["target"].value_counts().sort_index())

print("=" * 50)
import numpy as np
import pandas as pd

from datasets import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)

# ============================================
# Load Dataset
# ============================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("reddit_clean.csv")

print(df.head())
print()
print("Total Records :", len(df))
print()

# ============================================
# Train-Test Split
# ============================================

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["target"]
)

train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

print("Training Samples :", len(train_dataset))
print("Testing Samples  :", len(test_dataset))
print()

# ============================================
# Load Tokenizer
# ============================================

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# ============================================
# Tokenization
# ============================================

def tokenize_function(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )

train_dataset = train_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

# Rename target → labels
train_dataset = train_dataset.rename_column("target", "labels")
test_dataset = test_dataset.rename_column("target", "labels")

# Set PyTorch format
train_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "labels"]
)

test_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "labels"]
)

# ============================================
# Load BERT Model
# ============================================

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=5
)

# ============================================
# Metrics
# ============================================

def compute_metrics(eval_pred):

    logits, labels = eval_pred

    predictions = np.argmax(logits, axis=-1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        predictions,
        average="weighted"
    )

    accuracy = accuracy_score(labels, predictions)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

# ============================================
# Data Collator
# ============================================

data_collator = DataCollatorWithPadding(
    tokenizer=tokenizer
)

# ============================================
# Training Arguments
# ============================================

training_args = TrainingArguments(
    output_dir="results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_steps=50,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    greater_is_better=True,
    save_total_limit=1,
    report_to="none"
)

# ============================================
# Trainer
# ============================================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
# ============================================
# Train Model
# ============================================

print("=" * 60)
print("Training Started...")
print("=" * 60)

trainer.train()

print("=" * 60)
print("Training Completed")
print("=" * 60)

# ============================================
# Evaluate
# ============================================

results = trainer.evaluate()

print()
print("=" * 60)
print("Evaluation Results")
print("=" * 60)

for key, value in results.items():
    print(f"{key} : {value}")

# ============================================
# Save Model
# ============================================

trainer.save_model("mental_health_bert")
tokenizer.save_pretrained("mental_health_bert")

print()
print("=" * 60)
print("BERT Model Saved Successfully")
print("Folder : mental_health_bert")
print("=" * 60)
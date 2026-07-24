import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# ======================================================
# Load Trained Model
# ======================================================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(CURRENT_DIR, "mental_health_bert")

print("=" * 60)
print("Loading model from:")
print(MODEL_PATH)
print("=" * 60)

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

# Load trained model
model = BertForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model.eval()

# ======================================================
# Label Mapping
# ======================================================

labels = {
    0: "Stress",
    1: "Depression",
    2: "Bipolar Disorder",
    3: "Personality Disorder",
    4: "Anxiety"
}

# ======================================================
# Prediction Function
# ======================================================

def predict_mental_health(text: str):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        logits = outputs.logits

        probabilities = torch.softmax(logits, dim=1)

        predicted_class = torch.argmax(
            probabilities,
            dim=1
        ).item()

        confidence = probabilities[0][predicted_class].item()

    return {
        "prediction": labels[predicted_class],
        "confidence": round(confidence * 100, 2)
    }


# ======================================================
# Test Prediction
# ======================================================

if __name__ == "__main__":

    print("\nMental Health Prediction System")
    print("=" * 60)

    while True:

        text = input("\nEnter your feelings (type 'exit' to quit): ")

        if text.lower() == "exit":
            print("\nGoodbye!")
            break

        result = predict_mental_health(text)

        print("\nPrediction :", result["prediction"])
        print("Confidence :", result["confidence"], "%")
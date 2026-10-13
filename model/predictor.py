import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Option A: use Hugging Face Hub model (works immediately)
MODEL_PATH = "unitary/toxic-bert"


# Option B: if you later export your fine‑tuned toxic model, set MODEL_PATH = "model"
# and make sure pytorch_model.bin is inside that folder.

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.to(device)
model.eval()

LABELS = [
    "toxic",
    "severe_toxic",
    "obscene",
    "threat",
    "insult",
    "identity_hate"
]

PRIORITY = [
    "threat",
    "identity_hate",
    "severe_toxic",
    "obscene",
    "insult",
    "toxic"
]

def predict_comment(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.sigmoid(outputs.logits)[0]

    scores = {label: round(score.item() * 100, 2)
              for label, score in zip(LABELS, probabilities)}

    detected_labels = {label: score for label, score in scores.items() if score >= 50}

    if detected_labels:
        primary_category = "Toxic"
        for label in PRIORITY:
            if label in detected_labels:
                primary_category = label.replace("_", " ").title()
                break
    else:
        primary_category = "Non Toxic"

    if primary_category in ["Threat", "Identity Hate", "Severe Toxic"]:
        risk_level = "High"
    elif primary_category in ["Obscene", "Insult", "Toxic"]:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "primary_category": primary_category,
        "risk_level": risk_level,
        "detected_labels": detected_labels,
        "all_scores": scores
    }

from fastapi import FastAPI
from Schema.schemas import CommentRequest, PredictionResponse
from model.predictor import predict_comment

app = FastAPI(
    title="Toxic Comment Detection API",
    description="""
    Multi-label Toxic Comment Classification API using DistilBERT.

    Detects:
    - Toxic
    - Severe Toxic
    - Obscene
    - Threat
    - Insult
    - Identity Hate
    """,
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Toxic Comment Classifier API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy",
            "model": "DistilBERT",
            "version": "1.0.0"}

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(request: CommentRequest):

    result = predict_comment(request.text)

    return PredictionResponse(
        primary_category=result["primary_category"],
        risk_level=result["risk_level"],
        detected_labels=result["detected_labels"],
        all_scores=result["all_scores"]
    )
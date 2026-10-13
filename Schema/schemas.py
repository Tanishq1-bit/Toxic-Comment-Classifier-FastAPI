from pydantic import BaseModel,Field
from typing import Dict

class CommentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=2,
        max_length=5000,
        description="Comment to classify"
    )
class PredictionResponse(BaseModel):
    primary_category: str
    risk_level: str
    detected_labels: Dict[str, float]
    all_scores: Dict[str, float]
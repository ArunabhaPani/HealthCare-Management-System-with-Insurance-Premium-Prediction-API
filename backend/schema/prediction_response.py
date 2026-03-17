from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category : str = Field(
        ..., 
        description="Predicted insurance premium category", 
        example="medium")
        
    confidence : float = Field(
        ..., 
        description="Confidence of the prediction", 
        example=0.8)
        
    class_probabilities : Dict[str, float] = Field(
        ..., 
        description="Probabilities for each insurance premium category", 
        example={"low": 0.2, "medium": 0.5, "high": 0.3})
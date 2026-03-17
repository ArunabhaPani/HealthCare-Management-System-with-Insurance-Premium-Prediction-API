from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional, Literal, Optional

class Patient(BaseModel):
    id : Annotated[str, Field(..., description = "Unique identifier for the patient", example = "P001")]
    name : Annotated[str, Field(..., description = "Name of the patient", example = "John Doe")]
    city : Annotated[str, Field(..., description = "City where the patient resides", example = "New York")]
    age : Annotated[int, Field(..., gt = 0, lt = 120, description = "Age of the patient", example = 30)]
    gender : Annotated[Literal['male', 'female', 'other'], Field(..., description = "Gender of the patient", example = "male")]
    height : Annotated[float, Field(..., gt = 0, description = "Height of the patient in meters", example = 1.75)]
    weight : Annotated[float, Field(..., gt = 0, description = "Weight of the patient in kgs", example = 70.0)]

    @computed_field
    @property
    def bmi(self) -> float:
        '''Computed field to calculate BMI'''
        bmi =  round(self.weight / (self.height ** 2), 2)
        
        return bmi
    
    @computed_field
    @property
    def Verdict(self) -> str:
        '''Computed field to determine health risk based on BMI'''
        
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
        
class PatientUpdate(BaseModel):
    name : Annotated[Optional[str], Field(default = None)]
    city : Annotated[Optional[str], Field(default = None)]
    age : Annotated[Optional[int], Field(default = None, gt = 0, lt = 120)]
    gender : Annotated[Optional[Literal['male', 'female', 'other']], Field(default = None)]
    height : Annotated[Optional[float], Field(default = None, gt = 0)]
    weight : Annotated[Optional[float], Field(default = None, gt = 0)]
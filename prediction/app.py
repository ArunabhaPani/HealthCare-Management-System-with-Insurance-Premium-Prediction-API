from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION
  
app = FastAPI()

# Setting up the input data model


@app.get("/")
def read_root():
       return {"message": "Welcome to the Health Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

@app.get("/health")
def health_check():
       return {"status": "OK",
               "model_version": MODEL_VERSION,
               "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
       
       user_input = {
              'bmi': data.bmi,
              'lifestyle_risk': data.lifestyle_risk,
              'age_group': data.age_group,
              'city_tier': data.city_tier,
              'occupation': data.occupation,
              'income_lpa': data.income_lpa
       }

       try:
              prediction = predict_output(user_input)
              return JSONResponse(status_code=200, content={"response": prediction})
       
       except Exception as e:
              return JSONResponse(status_code=500, content={"error": str(e)})
       
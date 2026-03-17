from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION
from schema.patient_model import Patient, PatientUpdate
import json


app = FastAPI()

def load_data():
    '''Function to load initial data or configurations'''
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    '''Function to save data to the JSON file'''
    with open('patients.json', 'w') as f:
        json.dump(data, f)


@app.get("/")
def read_root():
       """Root endpoint to check API status"""
       return {"message": "Welcome to the Patient management System and Health Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}


@app.get('/about')
def about():
    """Endpoint to get information about the API"""
    return {"message": "Fully Functional Patient Management System API"}

@app.get('/view')
def view():
    """Endpoint to view patient data"""
    data = load_data()
    return {"data": data}

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., 
                                         description="The ID of the patient to retrieve",
                                         example="P001")):
    """Endpoint to view a specific patient's data by ID"""
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
    

@app.get('/sort')
def sort_patients(sort_by :str = Query(..., 
                                       description = 'Sort on the basis of height, weight or bmi'),
                    order : str = Query('asc', description = 'sort in asc or desc order')):
    """Endpoint to sort patients based on a specific attribute"""
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sort_order)
    
    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):
    """Endpoint to create a new patient record"""
    
    # load existing data
    data = load_data()
    
    #check if patient with same ID already exists
    if patient.id in data:
        raise HTTPException(status_code = 400, detail="Patient with this ID already exists")
    
    # add new patient
    data[patient.id] = patient.model_dump(exclude = ['id'])

    # save updated data back to json file
    save_data(data)

    return JSONResponse(status_code = 201, content={"message": "Patient created successfully"})


@app.put('/update/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    """ Endpoint to update an existing patient's data """
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient_info = data[patient_id]

    update_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in update_patient_info.items():
        existing_patient_info[key] = value

    # existing_patient_info -> pydantic object -> updated bmi  + verdict 
    
    existing_patient_info['id'] = patient_id  # Ensure ID is included for Pydantic model creation
    patient_pydantic_object = Patient(**existing_patient_info)
    existing_patient_info = patient_pydantic_object.model_dump(exclude = 'id')
    # -> pydantic object -> dict
    data[patient_id] = existing_patient_info
    # save updated data back to json file
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": existing_patient_info})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    """ Endpoint to delete a patient record """
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]

    # save updated data back to json file
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})




# Setting up the input data model

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
       
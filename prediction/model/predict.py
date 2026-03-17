import pickle
import pandas as pd

# Importing the model 
with open('model/model.pkl', 'rb') as f:
       model = pickle.load(f)


MODEL_VERSION = "1.0.0"

# Get class labels from the model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input : dict):
       df = pd.DataFrame([user_input])

       predicted_class = model.predict(df)[0]

       probalities = model.predict_proba(df)[0]
       confidence = max(probalities)

       class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probalities)))
       

       return {'predicted_category': predicted_class,
                'confidence': round(confidence, 4), 
                'class_probabilities': class_probs}
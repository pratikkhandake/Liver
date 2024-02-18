#utils file
import pickle

# Load the pickled model
with open("liver.pkl", "rb") as f:
    model = pickle.load(f)

def predict_liver_disease(gender, age, tb, db, alkphos, sgpt, sgot, tp, alb, ag_ratio):
    # Convert gender to numerical value if needed
    # Perform any necessary preprocessing
    # Make prediction using the model
    prediction = model.predict([[age, tb, db, alkphos, sgpt, sgot, tp, alb, ag_ratio]])[0]
    return prediction

import numpy as np

from app.models.xgb_model import load_model
from app.utils.preprocessing import preprocess_data
from app.schemas.prediction import HouseData

# Cargar el modelo y el preprocesador
model = load_model()

def predict_price(data:HouseData):
    # Preprocesar los datos
    df = preprocess_data(data)
    
    # Hacer la predicción
    prediction = np.expm1(model.predict(df))
    
    return float(prediction[0])

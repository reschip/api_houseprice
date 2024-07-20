from xgboost import XGBRegressor
import pickle
import joblib

def load_model():
    #model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # Cargar el modelo desde el archivo
    loaded_model = joblib.load("app/models/xgbo_model.pkl")
    return loaded_model
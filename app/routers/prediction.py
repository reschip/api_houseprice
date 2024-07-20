from fastapi import APIRouter, HTTPException

from app.operations.prediction import predict_price
from app.schemas.prediction import HouseData

router = APIRouter()

@router.post("/predict")
def predict(data: HouseData):
    try:
        prediction = predict_price(data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

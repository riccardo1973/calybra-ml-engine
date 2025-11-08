from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Calybra ML Engine running"}

@app.post("/predict")
def predict():
    return {"prediction": "demo_value"}

from fastapi import FastAPI
app = FastAPI()
@app.get("/predict_body_mass_g/{bill_length_mm}/{flipper_length_mm}")
def predict_body_mass_g(bill_length_mm:float, flipper_length_mm:float):
    return 1.80749048 * bill_length_mm + 49.49315676*flipper_length_mm -5816.736051126896
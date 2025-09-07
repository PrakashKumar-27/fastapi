from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SimpleRequest(BaseModel):
    a: int
    b: int

@app.get("/addition")
def add(data: SimpleRequest):
    return data.a + data.b

@app.post("/subtract")
def subtract(data: SimpleRequest):
    return data.a - data.b

@app.post("/multiply")
def multiply(data: SimpleRequest):
    return data.a * data.b

@app.post("/divide")
def divide(data: SimpleRequest):
    if data.b == 0:
        return {"error": "Division by zero is not allowed"}
    return data.a / data.b

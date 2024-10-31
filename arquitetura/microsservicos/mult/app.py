from fastapi import FastAPI

app = FastAPI()

@app.get("/mult")
def mult(op1: float, op2: float):
    return  op1 * op2
    

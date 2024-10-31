from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/mult")
def mult(op1: float, op2: float):
    res = {}

    if op1 is None or op2 is None:
        raise HTTPException(status_code=400, detail="op1 ou op2 não informado")

    res['resultado'] = op1 * op2
    return res

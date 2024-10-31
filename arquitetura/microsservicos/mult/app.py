from fastapi import FastAPI, HTTPException

app = FastAPI(__name__)

@app.get("/mult")
def mult(op1: float, op2: float):
    res = {}

    if op1 is None or op2 is None:
        raise HTTPException(status_code=400, detail="op1 ou op2 não informado")
    
    res['resultado'] = op1 * op2
    return res

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

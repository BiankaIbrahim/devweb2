from fastapi import FastAPI

app = FastAPI(__name__)

@app.get("/mult")
def mult(op1: float, op2: float):
    res = {}

    if not op1 or not op2:
        res['resultado'] = "op1 ou op2 não informado"
        return res, 400

    res['resultado'] = op1 * op2
    return res, 200

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
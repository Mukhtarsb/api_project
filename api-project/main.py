from fastapi import FastAPI, Query, HTTPException
from typing import List
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sum1n/{n}")
def read_sum1n(n:int):
    res= 0
    for i in range (1,n+1):
        res+=i
    return {"result": res}

# curl http://localhost:8000/fibo?n=5





@app.get("/fibo")
async def fibo(n: int = Query(..., gt=0)):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for i in range(2, n):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        return fib


@app.post("/reverse")
async def reverse_string(string: str ):
    return string[::-1]




elements = []

elements = []

@app.put("/list")
async def add_element(item: dict):
    element = item.get('element')
    if element is None:
        return {"error": "invalid request"}
    elements.append(element)
    return {"elements": elements}

@app.get("/list")
async def get_list():
    return elements


from typing import Dict
from pydantic import BaseModel

class Expression(BaseModel):
    expr: str
@app.post("/calculator")
async def calculate(expression: Expression):
    try:
        num1, op, num2 = expression.expr.split(",")
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid expression")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            raise HTTPException(status_code=403, detail="Division by zero")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")

    return {"result":  result}
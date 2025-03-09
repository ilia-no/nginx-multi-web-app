from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"app": "numba 1"}
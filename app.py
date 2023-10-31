from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Added build on every push
    return {"Hello": "World"}

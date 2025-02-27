from fastapi import FastAPI

app = FastAPI()  # ✅ Make sure this exists

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

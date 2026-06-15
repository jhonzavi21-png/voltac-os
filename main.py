from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"voltac": "online"}

@app.post("/lead")
def lead(data: dict):
    text = data.get("lead", "")

    if "compra" in str(text):
        return {"voltia": "intención de compra detectada"}

    return {"voltia": "sin intención clara"}

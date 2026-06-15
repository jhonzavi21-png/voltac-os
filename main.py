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
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    html = """
    <html>
    <head>
        <title>Voltac Dashboard</title>
    </head>
    <body style="font-family: Arial; background:#0f172a; color:white; padding:20px">

        <h1>⚡ Voltac Dashboard</h1>

        <div style="padding:10px; background:#1e293b; margin:10px 0;">
            <h3>Estado del sistema</h3>
            <p>Voltac: ONLINE</p>
            <p>VoltIA: ACTIVE</p>
        </div>

        <div style="padding:10px; background:#1e293b; margin:10px 0;">
            <h3>Métricas</h3>
            <p>Leads procesados: 1+</p>
            <p>IA status: estable</p>
        </div>

        <div style="padding:10px; background:#1e293b;">
            <h3>Acciones</h3>
            <p>/lead → API IA</p>
        </div>

    </body>
    </html>
    """

    return html

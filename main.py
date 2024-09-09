from fastapi import FastAPI, Response, status
from random import choice

app = FastAPI()

damaged_systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life support": "LIF-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05",
}

current_system = choice(list(damaged_systems.keys()))

@app.get("/status")
async def get_status():
    return {"damaged_system": current_system}

@app.post("/teapot")
async def post_teapot():
    return Response(status_code=status.HTTP_418_IM_A_TEAPOT)

@app.get("/repair-bay", response_class=Response)
async def get_repair_bay():
    repair_code = damaged_systems[current_system]
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{repair_code}</div>
    </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")
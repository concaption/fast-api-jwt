"""
path: main.py

"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def health_check():
    return JSONResponse(status_code=200, content={"message": "OK"})
from fastapi import FastAPI,status
from pydantic import BaseModel


app=FastAPI()

@app.post("/request_body")
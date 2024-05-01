from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

# serve static files
app.mount("/static", StaticFiles(directory="static"), name = "static")

class Message(BaseModel):
    content: str 


@app.get("/", response_class=HTMLResponse)
async def read__index():
    with open(os.path.join('static', 'index.html'), 'r') as f:
        return HTMLResponse(content = f.read())
    

@app.post("/chat/", response_model = Message)
async def recieve_message(message:Message):
    print(f"Received message: {message.content}")
    return JSONResponse(content={"content": message.content})
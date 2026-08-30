from fastapi import FastAPI, Body
from ollama import Client

client = Client()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact-us")
def read_root():
    return {"email": "rinkeshtest@gmail.com"}


@app.post("/chat")
def chat(message:str =  Body(...,description="The message")):
    response = client.chat(model="qwen2.5:1.5b",messages=[
        {"role":"user","content":message}
    ])
    
    return {"response":response.message.content}
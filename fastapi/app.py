from fastapi import FastAPI, Response
import requests

# create an instance of FastAPI class
# This object is essential for defining routes, handling requests, 
# and managing the application's lifecycle in a FastAPI project.
app = FastAPI()

# create a get route(endpoint)
@app.get('/')
def home():
    return {"hello":"world"}

# create a get route to ask ollama locally!
@app.get('/ask')
def ask(prompt: str):
    response = requests.post('http://localhost:11434/api/generate',json={
        "prompt": prompt,
        "stream" : False,
        "model" : "llama2" 
    })
    
    return Response(content=response.text, media_type="application/json" )

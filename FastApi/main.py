# from tarfile import data_filter
from fastapi import FastAPI
import json

app = FastAPI()

# load the json file data
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return{'message':'Patient management system API'}

@app.get("/view")
def View():
    data = load_data()
    return data

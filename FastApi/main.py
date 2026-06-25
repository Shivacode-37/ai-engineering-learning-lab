from fastapi import FastAPI, Path, HTTPException, Query
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
@app.get('/patient/{patient_id}')
def view_patient(patient_id :str = Path(..., description = 'ID of the patient in the Database', example='P001' )): # Path is defined
    # load all patients data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail="Patient not found") # HTTPException code raise

@app.get('/sort')
def sort_patients(sort_by: str =Query(..., description="Sort on the basis of height, weight, bmi"), order: str = Query('asc', description ="Order should be in asc and desc")):
    required_fields = ['height', 'weight', 'bmi']
    if sort_by not in required_fields:
        return HTTPException(status_code=404, detail=f'Invalid field is selected from {required_fields}')
    if order not in ['asc','desc']:
        return HTTPException(status_code=404, detail ="Invalid order is select, select in asc or desc")
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x :x.get(sort_by,0), reverse = sort_order)

    return sorted_data



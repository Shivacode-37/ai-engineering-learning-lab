from typing import Annotated, Literal, Optional
from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(..., description='Id of the patient', json_schema_extra=[{'example':'P001'}])]
    name : Annotated[str, Field(..., description= 'name of the patient', max_length=50)]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    weight  : Annotated[float, Field(..., description='weight of the patient')]
    height  : Annotated[float, Field(..., description='height of the patient')]
    age : Annotated[int,Field(...,gt=0, lt=100, description='Age of the patient')]
    gender : Annotated[str, Field(..., description='Gender of the patient')]


    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def diagnosis(self)->str:
        if self.bmi >18:
            return 'underweight'
        elif self.bmi >25:
            return 'Normal'
        elif self.bmi>30:
            return 'Normal'
        else:
            return 'obese'

class patientupdate(BaseModel):

    name : Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None, gt =0)]
    weight : Annotated[Optional[float], Field(default=None, gt =0)]
    height : Annotated[Optional[float], Field(default=None, gt =0)]
    gender : Annotated[Optional[Literal['male','female']], Field(default=None)]
# load the json file data
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)
@app.get("/")
def hello():
    return{'message':'Patient management system API'}

@app.get("/view")
def View():
    data = load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id :str = Path(..., description = 'ID of the patient in the Database', examples='P001' )): # Path is defined
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


@app.post('/create')
def create_patient(patient:Patient):
    data = load_data() # loading the data
    if patient.id in data:
        raise HTTPException(status_code=404,detail='Patient is already exist')

    # new patient add in data
    data[patient.id]=patient.model_dump(exclude=['id'])
    # saving the new patient record in the system
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'Patient added successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id :str, patient_update:patientupdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    current_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        current_patient_info[key] = value
# current_patient_info -> pydantic object -> updated bmi & vedict -> pydantic object -> dict
    current_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**current_patient_info)

    current_patient_info =patient_pydantic_object.model_dump(exclude='id')
    # add this dictionary to data
    data[patient_id] = current_patient_info

    # save the data
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'Patient updated successfully'})


@app.delete('/delete/{patient_id}')
def delete_patient_id(patient_id : str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'Patient ID deleted successfully'})


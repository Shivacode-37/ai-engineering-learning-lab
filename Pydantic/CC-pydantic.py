from typing import Annotated, Dict, List, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, computed_field, field_validator, model_validator


class Patient(BaseModel):
   name : Annotated[str, Field(max_length = 50, title = 'Name of the patient', description ='Give the name of the patient less than 50 characters', json_schema_extra={
        "example": ["Mohit", "Nikhil Agarwal"]
    })]
   age : int = Field(gt=0, le =100)
   email : EmailStr
   married : Annotated[bool, Field(default=None, description='Are you married or single?')]
   allergies : Annotated[Optional[List[str]], Field(default=None, max_length=5)]
   weight : Annotated[float, Field(gt=0, strict=True)]
   contact_details : Dict[str, str]
   linkdin_url : AnyUrl

class Patients(BaseModel):
    name : str
    age : int
    email : EmailStr
    married : Optional[bool]
    contact_details : dict[str, str]
    linkdin_url : AnyUrl
    weight : float
    height: float

    @field_validator('name')
    @classmethod
    def name_uppercase(cls,value):
        return value.upper()

    @field_validator('email')
    @classmethod
    def valid_email(cls,value):
        valid_mail =['sbi.in','pnb.in']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_mail:
            raise ValueError('Email is not valid')
        return value

    @model_validator(mode='after')
    def emergency_conatct_details(cls,value):
        # if value['age']>65 and 'emergency_contact' not in value['contact_details']: --> mode ='before'
        if value.age>65 and 'emergency_contact' not in value.contact_details:
            raise ValueError('Age is above then 65 required emergency contact details')
        return value
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def update_patient_info(patient:Patients):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.linkdin_url)
    print(patient.email)
    print(patient.contact_details)
    print('BMI',patient.bmi)
patient_details_info = {'name':'isha', 'age':75, 'email': '0429@sbi.in', 'married':False, 'weight':55.5, 'height':160.3, 'contact_details':{'phone':'837783787', 'emergency_contact':'8394837477'},'linkdin_url':'https://1111.com'}
patient2 = Patients(**patient_details_info)

update_patient_info(patient2)

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.linkdin_url)
    print(patient.email)
    print(patient.contact_details)
patient_details = {'name':'Shiva', 'age':25, 'email': '7890@gmail.com', 'weight':69, 'contact_details':{'phone':'678906789'},'linkdin_url':'https://1313.com'}
patient1 = Patient(**patient_details)

update_patient_data(patient1)












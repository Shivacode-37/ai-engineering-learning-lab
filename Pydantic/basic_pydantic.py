from pydantic import BaseModel

class Patient(BaseModel):
    name :str
    age : int


def insert_patient_details(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('details inserted')

def updated_patient_details(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('details updated')

patient_information = {'name':'shiva','age':25}
# **unpack tuples
patient1 = Patient(**patient_information)
patient2 = Patient(**patient_information)

updated_patient_details(patient1)

insert_patient_details(patient2)


# Nested_models
from pydantic import BaseModel

class contact(BaseModel):
    phone: str
    emergency_contact_details: str

class person(BaseModel):
    name:str
    age: int
    contact_details:contact

person_details = person(name = 'Mohit', age=25, contact_details={'phone':'7479835232','emergency_contact_details':'436432432'})


p1 =person_details.model_dump(exclude=['age'])
print(p1)

# Serialization

class Address(BaseModel):
    city : str
    state : str
    address: str

class student(BaseModel):
    name : str
    age : str
    pin :str ='176025'
    address : Address
address_dict ={'city':'Kangra','state':'Himachal Pradesh','address':'Jagnoli, kangra'}
address1 = Address(**address_dict)
student_dict = {'name':'Rohit','age':'25','address':address1}

student1=student(**student_dict)

s1 = student1.model_dump(exclude_unset=True)
print(s1)




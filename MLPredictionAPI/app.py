from fastapi import FastAPI
from pydantic import BaseModel, computed_field,Field, field_validator
from typing import Annotated, Literal
import pickle
import pandas as pd
from fastapi.responses import JSONResponse

# import the ml model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune","Chandigarh","Indore"]
tier_2_cities = [
    "Jaipur", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"]

class userdata(BaseModel):
    age : Annotated[int, Field(..., description="Age of the user", gt =0)]
    weight : Annotated[float, Field(...,  description='Weight of the user', gt =25)]
    height : Annotated[float, Field(...,  description='height of the user', gt =25)]
    income_lpa : Annotated[int, Field(..., description='Annual income of the user')]
    smoker : Annotated[bool, Field(..., description='Is user smoker?')]
    city : Annotated[str, Field(..., description='The city from user belongs')]
    occupation : Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='The occupation of the user')]

    @field_validator('city')
    @classmethod
    def city_name(cls,name_correction:str)-> str:
        name_correction = name_correction.strip().title()
        return name_correction

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def life_risk(self)-> str:
        if self.smoker and self.bmi > 30:
            return "High"
        elif self.smoker and self.bmi > 26:
            return 'Medium'
        else:
            return 'Low'
    @computed_field
    @property
    def age_info(self)-> str:
        if self.age<25:
            return 'Young'
        elif self.age<35:
            return 'Adult'
        elif self.age<50:
            return 'Middle aged'
        else:
            return 'Senior'

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3


@app.get('/')
def Home():
     return {'messgae':'This is the Insurance ML prediction API'}


@app.post('/predict')
def predict_insurance_premium(data:userdata):
    input_value = pd.DataFrame([{'bmi': data.bmi,
                                  'age_info': data.age_info,
        'life_risk': data.life_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation}])
    prediction = model.predict(input_value)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
    

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()


# schema
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="Write down all the pros inside a list"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="Write down all the cons inside a list"
    )
    name: Optional[str] = Field(
        default=None, description="Write the name of the reviewer"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
BMW is a premium German automobile company known for luxury,
performance, advanced technology, and sporty driving experience.
The brand manufactures luxury cars, SUVs, electric vehicles,
and high-performance M series cars.

BMW cars are popular for:
- Powerful engines
- Premium interior quality
- Modern technology features
- Excellent driving dynamics
- Stylish and sporty design

Some famous BMW series include:
- BMW 3 Series
- BMW 5 Series
- BMW 7 Series
- BMW X Series SUVs
- BMW M Performance models

Pros:
- Luxury and comfort
- Strong performance
- Advanced safety features
- Premium brand value

Cons:
- High maintenance cost
- Expensive spare parts
- Lower mileage compared to economy cars

Overall, BMW is considered one of the top luxury car brands
in the world for people who want performance, comfort,
and premium driving experience.
review by Mohit
""")

print(result)

from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",  # show error because it doesn't support with_structure_output we need Output parser
)

model = ChatHuggingFace(llm=llm)


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

result = structured_model.invoke("""he Triumph Speed 400 is a premium modern-retro bike that combines classic Triumph styling with strong performance and everyday comfort. It comes with a 398cc liquid-cooled engine producing around 40 PS power, making it smooth, refined, and fun for both city rides and highways.Key highlights include:Premium build qualityComfortable riding postureGood handling and stabilityDual-channel ABS and traction controlStylish retro-modern design ProsSmooth and powerful enginePremium look and feelEasy to handle for beginnersGood balance for city + touringConsSlight engine heat in trafficRear suspension feels stiff sometimesLimited service network compared to bigger brandsPillion comfort is average for long ridesOverall, the Speed 400 is one of the best all-rounder bikes in the 400cc segment for riders wanting a premium, stylish, and refined motorcycle. Summarize by Shiva
""")

print(result)

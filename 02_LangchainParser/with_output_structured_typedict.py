from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal

load_dotenv()

model = ChatOpenAI()


class Bike(TypedDict):
    summary: Annotated[str, "A brief summary of bike model is 2026"]
    features: Annotated[list[str], "Feature of bike and aslo the colors"]
    pros: Annotated[Literal["Pos", "Neg"], "Just say Positive as 1 and Negative as 0"]
    name: Annotated[str, "Reviewd by the person"]


struct_model = model.with_structured_output(Bike)

result = struct_model.invoke(
    "The Triumph Speed 400 is a premium modern-retro bike that combines classic Triumph styling with strong performance and everyday comfort. It comes with a 398cc liquid-cooled engine producing around 40 PS power, making it smooth, refined, and fun for both city rides and highways.Key highlights include:Premium build qualityComfortable riding postureGood handling and stabilityDual-channel ABS and traction controlStylish retro-modern design ProsSmooth and powerful enginePremium look and feelEasy to handle for beginnersGood balance for city + touringConsSlight engine heat in trafficRear suspension feels stiff sometimesLimited service network compared to bigger brandsPillion comfort is average for long ridesOverall, the Speed 400 is one of the best all-rounder bikes in the 400cc segment for riders wanting a premium, stylish, and refined motorcycle. Summarize by Shiva"
)

print(result["name"])

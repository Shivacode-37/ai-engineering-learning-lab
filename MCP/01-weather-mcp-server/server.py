import httpx
from mcp.server import MCPServer

mcp = MCPServer("Weather")

async def get_coordinates(city:str)-> str:  # Internal
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count" :1
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url,params=params)
        response.raise_for_status()
        data = response.json()

    if not data.get("results"):
        return None
    location = data["results"][0]

    return {
        "name": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "country": location.get("country")   }
async def get_current_weather(latitude:float, longitude:float):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude":latitude,
        "longitude":longitude,
        "current":"temperature_2m,wind_speed_10m,weather_code"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params =params)
        response.raise_for_status()
        data = response.json()

        current = data["current"]

        return {
            "temperature": current["temperature_2m"],
            "wind_speed": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
}


@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the current weather of the city."""

    location = await get_coordinates(city)

    if location is None:
        return f"Could not find location: {city}"

    weather = await get_current_weather( location["latitude"],location["longitude"])

    return (
    f"Weather in {location['name']}, {location['country']}:\n"
    f"🌡 Temperature: {weather['temperature']}°C\n"
    f"💨 Wind Speed: {weather['wind_speed']} km/h\n"
    f"🛰 Partly cloud: {weather['weather_code']}"
)

@mcp.resource("cities:// supported", name = "Supported Cities", description="List of the cities supported by the weather MCP Server",
              mime_type="text/Plain")
def supported_cities()-> str:
    """ list of supported cities"""
    return """
Delhi
Mumbai
London
Tokyo
Japan
Bangalore
"""
@mcp.prompt(
    name="Weather_Genie",
    description="Analyze weather and provide recommendations"
)
def weather_genie():
    return """
You are a weather genie.

Based on the weather information:

- Summarize the weather.
- Recommend clothing.
- Tell the user if they should carry an umbrella.
- Keep the answer under 120 words"""

if __name__ == "__main__":
    mcp.run()


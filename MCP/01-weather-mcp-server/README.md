# 🌦 Weather MCP Server

My first MCP (Model Context Protocol) server built using the official Python MCP SDK.

## Features

- MCP Tool: Get Current Weather
- Open-Meteo Geocoding API
- Open-Meteo Weather API
- Async HTTP requests using httpx
- Tested using MCP Inspector

## Tech Stack

- Python 3.11
- MCP Python SDK v2
- httpx
- Open-Meteo API

## Architecture

User
↓
MCP Inspector
↓
Weather MCP Server
↓
get_coordinates()
↓
Geocoding API
↓
get_current_weather()
↓
Weather API
↓
Response

## Learning Outcomes

- Built first MCP Tool
- Learned async/await
- Integrated external APIs
- Understood Tool orchestration
- Debugged HTTP API integration

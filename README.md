# T11

T11 Voice Assistant
A voice assistant implementation using ElevenLabs for text-to-speech synthesis. The system provides real-time voice interaction capabilities through a FastAPI backend server with WebSocket support.

Key Features
Text-to-speech synthesis using ElevenLabs API
Real-time WebSocket communication
Twilio integration for voice calls
Secure tunnel setup via ngrok
Environment variable management for API keys

Tech Stack
Python
FastAPI
ElevenLabs
Twilio
WebSocket
ngrok

Project Structure
CopyT11/
├── run_server.py     # Main server application
├── .env             # Environment variables
└── venv/            # Virtual environment

Setup and Run Instructions
Prerequisites

Python 3.x
ngrok installed
Git installed

Installation Steps

Create and activate virtual environment:
python -m venv venv
.\venv\Scripts\Activate.ps1

Upgrade pip and install dependencies:
pip install --upgrade pip
pip install python-dotenv elevenlabs fastapi psutil requests twilio uvicorn websockets

Run the server:
python run_server.py

Start ngrok tunnel:
& "C:\Program Files\ngrok\ngrok.exe" http 8000

Environmental Variables
Create a .env file in the root directory with:
Required API keys and configuration
(Add your specific env variables here)
ELEVENLABS_API_KEY=
AGENT_ID=
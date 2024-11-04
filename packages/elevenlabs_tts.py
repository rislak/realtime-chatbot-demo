import os
import requests
from dotenv import load_dotenv
from elevenlabs import play

load_dotenv()

# Get API key from environment
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # Default voice, can be changed

def speak(text):
    try:
        #Based on elevenlabs docs, streaming reducing latency
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}/stream"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
        }

        # Used Turbo v2.5 for lower latency
        data = {
            "text": text,
            "model_id": "eleven_turbo_v2_5",  
        }

        # Make a streaming request to gather audio chunks
        response = requests.post(url, headers=headers, json=data, stream=True)
        response.raise_for_status()

        audio_data = bytearray()
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                audio_data.extend(chunk)
        
        play(audio_data)

    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}")

import openai
import os
from playsound import playsound

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt and parameters for the API request
prompt = "Hello, how are you doing today?"
model = "text-to-speech/whisper-1"
voice = "eng-USA"
speed = 0.9
response_format = "mp3"

# Call the API to generate speech
response = openai.TtsV3.create(
    prompt=prompt,
    model=model,
    voice=voice,
    speed=speed,
    format=response_format
)

# Save the generated speech to an MP3 file
with open("generated_speech.mp3", "wb") as f:
    f.write(response.audio)

# Play the generated speech using the playsound library
playsound("generated_speech.mp3")




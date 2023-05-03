import requests
import json
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt and parameters for the API request
prompt = "A yellow bird with a short beak and a white belly"
model = "image-alpha-001"
response_format = "url"

# Call the API to generate an image
response = openai.Image.create(
    prompt=prompt,
    model=model,
    response_format=response_format
)

# Extract the generated image URL from the API response
image_url = response["data"][0]["url"]

# Download the image to a file
response = requests.get(image_url)
with open("generated_image.png", "wb") as f:
    f.write(response.content)

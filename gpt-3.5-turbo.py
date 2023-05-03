import openai
import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt and parameters for the API request
prompt = "Hello, what can you help me with today?"
model = "text-davinci-002"
temperature = 0.7
max_tokens = 100
stop = "\n"

# Call the API to generate a response
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    stop=stop
)

# Extract the generated response from the API response
generated_text = response.choices[0].text.strip()

# Print the generated response
print(generated_text)

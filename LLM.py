import openai
import json

# Load JSON file
with open("screen_time_data.json", "r") as file:
    screen_time_data = json.load(file)

# Convert JSON to a string (if needed)
json_string = json.dumps(screen_time_data, indent=2)

# OpenAI API call
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",  # Use GPT-4 or the latest available model
    messages=[
        {"role": "system", "content": "You are an AI assistant that provides productivity and mental health insights based on screen time data."},
        {"role": "user", "content": f"Here is my screen time data:\n{json_string}\n\nPlease analyze it and provide suggestions for productivity and mental health."}
    ],
    temperature=0.7,
    max_tokens=500
)

# Print response
print(response["choices"][0]["message"]["content"])

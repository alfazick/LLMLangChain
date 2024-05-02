from openai import OpenAI

import os
api_key = os.getenv('API_KEY')

# creating the model to be used
client = OpenAI(api_key = api_key)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi, my name is Alex."}]
)

print(completion)
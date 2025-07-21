import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=api_key)

models = client.models.list()

print("Available models:")
for model in models:
    print(model.id)

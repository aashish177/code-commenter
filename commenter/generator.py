import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_comment(function_details):
    """ 
    Generate a Python docstring for a given function using OPENAI GPT-4 Turbo.
    """
    prompt = f"Write a concise Python docstring for the function:\n\n"
    prompt += f"def{function_details['name']}({', '.join(function_details['args'])}):\n"

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}],
        max_tokens = 100
    )

    return response.choices[0].message.content.strip()

#Test the function
if __name__ == "__main__":
    sample_function = {"name": "add", "args": ["a", "b"], "lineno": 2}
    print(generate_comment(sample_function))
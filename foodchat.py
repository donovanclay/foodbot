import os
import openai


# openai.api_key = os.getenv("")
openai.api_key = os.getenv('OPENAI_KEY')

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# print(generate_response(input("Prompt: ")))
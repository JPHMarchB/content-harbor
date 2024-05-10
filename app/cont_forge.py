from typing import List
from dotenv import load_dotenv
import os
from openai import OpenAI
import argparse
import re
load_dotenv()


def content_generation(prompt: str):
    api_key=os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Generate a topic for a social media post based on current events relating to {prompt}, no hashtags"}], 
    max_tokens=32, 
    temperature=0.6
    )

    # Get generated response
    response: str = completion.choices[0].message.content

    # Remove extra whitespace in response
    response = response.strip()

    # Check if last character in response is a punctuation
    last_char = response[-1]

    # If not add elipses to the end of the response
    if last_char not in {".", "!", "?",'"'}:
        response += '..."'

    # Return the final response
    print(response)
    return response

def keyword_generation(prompt: str) -> List[str]:
    api_key=os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Generate keywords relating to {prompt}, do not number them"}], 
    max_tokens=32, 
    temperature=0.6
    )

    response: str = completion.choices[0].message.content
    response = response.strip()

    response = response.strip()
    keywords_array = re.split(",|\n|;|-", response)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 1]

    print(keywords_array)
    return keywords_array


def validate_request_length(prompt: str) -> bool:
    return len(prompt) <= 24


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", 
        "-i", 
        type=str, 
        required=True
        )
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")

    if validate_request_length(user_input):
        content_generation(user_input)
        keyword_generation(user_input)
    else:
        raise ValueError(f"Your prompt is too long! Please keep it under 24 characters. Your input was {len(user_input) - 24} characters too long.")


if __name__ == "__main__":
    main()
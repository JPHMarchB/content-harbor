from typing import List
from dotenv import load_dotenv
import os
from openai import OpenAI
import argparse
import regex
load_dotenv()


def content_generation(prompt: str):
    api_key=os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Generate a topic for a social media post based on current events relating to {prompt}"}], 
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
    if last_char not in {".", "!", "?", '"'}:
        response += "..."

    # Return the final response
    return response


def keyword_generation(prompt: List[str]):
    api_key=os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Generate keywords relating to {prompt}"}], 
    max_tokens=32, 
    temperature=0.6
    )

    response: str = completion.choices[0].message.content
    response = response.strip()

    # Take keywords, turn them into array
    keyword_array = regex.split(",|\n|.|-", response)

    # Remove white spaaces
    keyword_array = [k.strip() for k in keyword_array]
    
    # Get rid of null values
    keyword_array = [k for k in keyword_array if len(k) > 0]
    return keyword_array

def main():
    print("Running process")

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
    content_result = content_generation(user_input)
    keywords_result = keyword_generation(user_input)
    
    print(content_result)
    print(keywords_result)


if __name__ == "__main__":
    main()
from dotenv import load_dotenv
import os
from openai import OpenAI
import argparse
load_dotenv()
api_key=os.environ.get("OPENAI_API_KEY")

def content_generation(prompt: str):
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You're a social media assistant adept at crafting engaging content ideas for professionals and content creators social media posts"},
        {"role": "user", "content": f"Generate a social media post idea for '{prompt}'"}], 
    max_tokens=32, 
    temperature=0.6
    )

    print(completion.choices[0].message)


def main():
    print("Running processes")

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
    content_generation(user_input)
    pass


if __name__ == "__main__":
    main()
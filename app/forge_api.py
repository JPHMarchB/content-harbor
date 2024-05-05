from typing import Union
from fastapi import FastAPI
from cont_forge import content_generation, keyword_generation, validate_request_length

app = FastAPI()

@app.get("/generate_content")
async def content_generation_api(prompt: str):
    validate_request_length(prompt)
    snippet = content_generation(prompt)
    return {"Snippet": snippet}

@app.get("/generate_keywords")
async def keyword_generation_api(prompt: str):
    validate_request_length(prompt)
    keywords = keyword_generation(prompt)
    return {"keywords": keywords}

@app.get("/post_idea")
async def post_generation_api(prompt: str):
    validate_request_length(prompt)
    concept = content_generation(prompt) 
    keywords = keyword_generation(prompt)
    return {"Post Concept": concept, "Post Keywords": keywords}

# fastapi dev forge_api.py
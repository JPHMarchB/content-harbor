from fastapi import FastAPI, HTTPException
from cont_forge import content_generation, keyword_generation
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/generate_content")
async def content_generation_api(prompt: str):
    request_validation(prompt)
    snippet = content_generation(prompt)
    return {"Snippet":snippet,"keywords":[]}

@app.get("/generate_keywords")
async def keyword_generation_api(prompt: str):
    request_validation(prompt)
    keywords = keyword_generation(prompt)
    return {"snippet":None,"keywords":keywords}

@app.get("/post_idea")
async def post_generation_api(prompt: str):
    request_validation(prompt)
    concept = content_generation(prompt) 
    keywords = keyword_generation(prompt)
    return {"Post Concept":concept,"Post Keywords":keywords}

def request_validation(prompt: str):
    if len(prompt) > 24:
        raise HTTPException(status_code=400, detail="Prompt length exceeds maximum allowed length of 24 characters")

# fastapi dev forge_api.py
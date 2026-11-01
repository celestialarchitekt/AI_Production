
from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="LangGraph Render Agent")

client = OpenAI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def health_check():
    return {"status": "online", "message": "Agent backend is running!"}

@app.post("/run-agent")
def run_agent(request: PromptRequest):
    try:
        # Placeholder for your LangGraph invocation or direct OpenAI call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": request.prompt}
            ]
        )
        return {
            "success": True, 
            "result": response.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
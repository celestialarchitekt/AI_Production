"""
==============
FastAPI Server
==============
"""

# env VARs
from dotenv import load_dotenv
load_dotenv(override=True)


# imports
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI(title="LangGraph Render Agent")

# OpenAI API
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)


class PromptRequest(BaseModel):
    prompt: str

# root
@app.get("/")
def health_check():
    return {"status": "online", "message": "Agent backend is running!"}


# run agent
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
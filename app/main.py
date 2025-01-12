from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

# Verify required environment variables
if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set in the .env file.")
if not GITHUB_ACCESS_TOKEN:
    raise EnvironmentError("GITHUB_ACCESS_TOKEN is not set in the .env file.")

# Initialize FastAPI app
app = FastAPI()

# Import and include routers
from app.routes.analyze import router as analyze_router

app.include_router(analyze_router)

# Root endpoint for health check
@app.get("/")
def root():
    return {"message": "API is running!"}

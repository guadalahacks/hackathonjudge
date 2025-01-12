import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
client = openai.OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_quality(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an evaluator scoring text for clarity, innovation, and relevance."},
                {"role": "user", "content": f"Evaluate the following text and provide just a score from 0 to 10:\n\n{text}"}
            ]
        )
        score = float(response.choices[0].message.content.strip())

        return max(0, min(score, 10))
    except Exception as e:
        raise ValueError(f"Error analyzing text quality: {str(e)}")

def analyze_code_quality(repo_url):
    return 8  # Placeholder for actual analysis

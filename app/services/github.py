from github import Github
from app.services.scoring import analyze_text_quality, analyze_code_quality
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def analyze_github(github_url):
    token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(token)

    try:
        repo_name = github_url.split('github.com/')[-1]
        repo = g.get_repo(repo_name)

        readme_content = repo.get_readme().decoded_content.decode()
        commits = repo.get_commits()

        
        code_quality = 8  # Placeholder for actual code analysis
        readme_score = analyze_text_quality(readme_content)

        code_score = round((0.9 * code_quality + 0.1 * readme_score), 2)

        return {"code_score": code_score}
    except Exception as e:
        raise ValueError(f"Unable to analyze GitHub repository: {str(e)}")

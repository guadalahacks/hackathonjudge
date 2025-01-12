from fastapi import APIRouter, HTTPException
from app.models.schemas import ProjectInput, ProjectOutput
from app.services.devpost import analyze_devpost
from app.services.github import analyze_github

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.post("/", response_model=ProjectOutput)
async def analyze_project(input: ProjectInput):
    try:
        devpost_data = analyze_devpost(input.devpost_url)
        github_data = analyze_github(input.github_url)

        # Scoring Calculation
        code_score = github_data["code_score"]
        total_score = round(
            0.4 * devpost_data["summary_score"] + 0.6 * code_score, 2
        )

        return ProjectOutput(
            title=devpost_data["title"],
            summary=devpost_data["summary"],
            code_score=code_score,
            total_score=total_score
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

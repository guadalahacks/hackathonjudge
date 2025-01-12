from pydantic import BaseModel

class ProjectInput(BaseModel):
    devpost_url: str
    github_url: str

class ProjectOutput(BaseModel):
    title: str
    summary: str
    code_score: float
    total_score: float
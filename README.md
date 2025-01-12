# Hackathonjudge
Hackathonjudge evaluates projects from Devpost and GitHub by extracting project details and analyzing code quality. It provides a score for the project’s description and code, calculating a total score based on both.
\
**Goal:** Automate hackathon project evaluation.


## Instructions for developers
1. Clone repo

2. cd to path

3. Create virtual enviroment:
python3 -m venv venv
or
py -m venv venv

4. Activate virtual enviroment: \
Windows: venv\Scripts\activate \
macOS/Linux: source venv/bin/activate

**If script execution is disabled:** \
Windows: \
    - Open PowerShell as an administrator. \
    - Run the following command to set the execution policy to allow scripts to run: \
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser \
    - Confirm the change by typing Y and pressing Enter.

5. Install requirements \
pip install -r requirements.txt

**For testing**
1. pip install pytest pytest-asyncio

## Running the API
uvicorn app.main:app --reload

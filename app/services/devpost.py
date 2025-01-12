import requests
from bs4 import BeautifulSoup
from app.services.scoring import analyze_text_quality

def analyze_devpost(devpost_url):
    response = requests.get(devpost_url)
    if response.status_code != 200:
        raise ValueError("Unable to access Devpost URL")

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').text.strip()
    summary = soup.find('meta', {'name': 'description'})["content"]

    summary_score = analyze_text_quality(summary)

    return {
        "title": title,
        "summary": summary,
        "summary_score": summary_score
    }

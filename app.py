import os
import pickle

MODEL_PATH = os.path.join("models", "matcher.pkl")

with open(MODEL_PATH, "rb") as f:
    matcher = pickle.load(f)

from flask import Flask, render_template, request
from nlp.resume_parser import extract_text_from_pdf
from nlp.skill_extractor import extract_skills
import pickle, os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "matcher.pkl")

with open(MODEL_PATH, "rb") as f:
    matcher = pickle.load(f)

JOB_SKILLS = ["python", "machine learning", "nlp", "flask", "mongodb", "git"]

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []
    if request.method == "POST":
        file = request.files["resume"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        text = extract_text_from_pdf(path)
        skills = extract_skills(text)
        score = round(matcher(skills, JOB_SKILLS) * 100, 2)

    return render_template("index.html", score=score, skills=skills)

if __name__ == "__main__":
    app.run()

SKILLS = [
    "python", "machine learning", "nlp", "flask",
    "mongodb", "rest api", "git", "sql"
]

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return list(set(found))

from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

def match(resume_skills, job_skills):
    vec1 = np.array([1 if s in resume_skills else 0 for s in job_skills]).reshape(1, -1)
    vec2 = np.ones((1, len(job_skills)))
    return cosine_similarity(vec1, vec2)[0][0]

pickle.dump(match, open("models/matcher.pkl", "wb"))

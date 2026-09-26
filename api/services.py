"""
Shared backend service functions.

This file will contain reusable logic for communication
between the API, AI services, and database services.

"""


"""
Updated 9.24.2026
Author: AndyVR
"""

def extract_resume_text(file):
    # TODO: implement PDF/DOCX parsing
    return "parsed text"

def parse_job_posting(data):
    # TODO: extract skills, requirements, etc.
    return {"parsed": True}

def build_analysis_prompt(resume_text, job_text):
    # TODO: create structured prompt for AI
    return f"Analyze resume vs job: {resume_text[:50]}..."

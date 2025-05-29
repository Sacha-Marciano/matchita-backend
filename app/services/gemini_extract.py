# services/gemini_extract.py
from vertexai.generative_models import GenerativeModel
import json
import re

gemini = GenerativeModel("gemini-2.0-flash-lite-001")


def clean_json_response(response_text: str):
    # Remove ```json ... ``` or ``` ... ``` if they surround the content
    if response_text.startswith("```") and response_text.endswith("```"):
        response_text = re.sub(r"^```(?:json)?\n?", "", response_text)
        response_text = re.sub(r"\n?```$", "", response_text)
    return response_text

def extract_answer(question: str, text: str ):
    prompt = (
        f"You are an intelligent assistant for our user. Answer the user's question using the content of the provided document.\n"
        f"- Be accurate and assertive, give a complete answer\n"
        f"- Answer as an assistant, the user needs to feel you help him a lot\n"
        f"- Do not hallucinate information outside the document.\n"
        f"Question:\n"
        f"{question}\n\n"
        f"Document :\n"
        f"{text}\n\n"
        f"Include the exact text you fetched your answer from"
        f"Respond only in JSON format with the following fields:\n"
        f"{{\"found\": true, \"answer\": \"...\", \"text_source\": \"...\"}}"
        f"If no answer was found respond this JSON:\n"
        f"{{\"found\": false}}"

    )

    response = gemini.generate_content(prompt)
    # Use streaming=False to simplify
    try:
        json_response_raw = response.text.strip()
        json_response_cleaned = clean_json_response(json_response_raw)
        parsed = json.loads(json_response_cleaned)
        return {"response" : parsed}
    except Exception as e:
        print("Gemini extract failed:", e)
        return None

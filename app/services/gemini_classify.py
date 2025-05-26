# services/gemini_classify.py
from vertexai.generative_models import GenerativeModel

gemini = GenerativeModel("gemini-pro")

def classify_document(text: str):
    prompt = f"""
You are an intelligent assistant. Classify the following document with:
- A descriptive title
- A folder name (short, thematic)
- 3 to 5 tags

Respond only in JSON format with: "title", "folder", and "tags".

Document:
{text[:4000]}
"""

    response = gemini.generate_content(prompt)
    # Use streaming=False to simplify
    try:
        json_response = response.text.strip()
        import json
        parsed = json.loads(json_response)
        return {
            "title": parsed["title"],
            "folder": parsed["folder"],
            "tags": parsed["tags"]
        }
    except Exception as e:
        print("Gemini parse failed:", e)
        return None

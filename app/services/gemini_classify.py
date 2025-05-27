# services/gemini_classify.py
from vertexai.generative_models import GenerativeModel

gemini = GenerativeModel("gemini-2.0-flash-lite-001")

def classify_document(text: str, folders: list[str] , tags: list[str] ):
    prompt = (
        f"You are an intelligent assistant. Classify the following document with:\n"
        f"- A descriptive title\n"
        f"- A folder name (short, thematic)\n"
        f"- 5 tags\n\n"
        f" Here is a list of existing folders that you may use if a folders matches for the following document : \n"
        f"{folders}\n\n"
        f"Only use the existing folders if they match perfectly, otherwise create new ones.\n"
        f"Here is a list of existing tags that you may use if a tag matches for the following document : \n"
        f"{tags}\n\n"
        f"Only use the existing tags if they match perfectly, otherwise create new ones.Be very specific when creating new tags\n"
        f"Respond only in JSON format with: \"title\", \"folder\", and \"tags\",  \n"
        f"do not include ``` json or any other formatting, like this : \n"
        f"{{\"title\": \"title\",\"folder\":\"folder\",\"tags\":\"tags\"}}\n\n"
        f"Document:\n"
        f"{text[:4000]}"
    )

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

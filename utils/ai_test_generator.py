import json
import urllib.request
import urllib.error
import os

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_tests_from_api(data: dict) -> str:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set.")

    prompt = f"""You are a Python test engineer. Given the following JSON response from an API, generate pytest test functions that validate:
- Required fields are present
- Field types are correct
- Field values are within expected ranges or formats (e.g. email format, non-empty strings)
- Edge cases relevant to the data

API Response:
{json.dumps(data, indent=2)}

Return ONLY valid Python pytest code. No explanations, no markdown fences. Start directly with imports."""

    payload = json.dumps({
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "Mozilla/5.0"
}

    req = urllib.request.Request(GROQ_API_URL, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Groq API error {e.code}: {e.read().decode()}")
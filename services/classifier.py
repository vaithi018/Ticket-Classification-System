import os
import json
from openai import OpenAI

def classify_ticket(description: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # Fallback if no API key is provided
        return {
            "category": "General Inquiry",
            "priority": "Medium",
            "team": "General"
        }
    
    try:
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Classify the following support ticket into a category, priority, and team.
        Respond in strict JSON format: {{"category": "...", "priority": "...", "team": "..."}}
        Ticket: {description}
        """
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error classifying ticket: {e}")
        return {
            "category": "Unknown",
            "priority": "Unknown",
            "team": "Unknown"
        }

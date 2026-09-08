import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

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
        # Smart keyword fallback if API quota or connection issue occurs
        desc_lower = description.lower()
        if any(w in desc_lower for w in ["database", "bug", "crash", "error", "500", "timeout"]):
            return {"category": "Bug", "priority": "High", "team": "Engineering"}
        elif any(w in desc_lower for w in ["billing", "charge", "payment", "invoice", "cost"]):
            return {"category": "Account/Billing", "priority": "High", "team": "Billing & Finance"}
        elif any(w in desc_lower for w in ["security", "auth", "login", "password", "hack"]):
            return {"category": "Security", "priority": "Critical", "team": "Security Team"}
        elif any(w in desc_lower for w in ["feature", "add", "dark mode", "ui", "request"]):
            return {"category": "Feature Request", "priority": "Low", "team": "Product"}
        return {
            "category": "General Inquiry",
            "priority": "Medium",
            "team": "Customer Support"
        }

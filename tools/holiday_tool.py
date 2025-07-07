# tools/holiday_tool.py
from datetime import datetime
from langchain_core.tools import tool
import requests

@tool
def check_public_holiday() -> str:
    """Check if today is a public holiday in Malaysia."""
    today = datetime.today().strftime("%Y-%m-%d")
    try:
        response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{datetime.today().year}/MY")
        holidays = response.json()
        for h in holidays:
            if h['date'] == today:
                return f"Today ({today}) is a public holiday: {h['localName']}"
        return f"Today ({today}) is not a public holiday."
    except Exception as e:
        return "Unable to check public holiday at this moment."

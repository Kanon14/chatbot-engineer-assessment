from datetime import datetime
import sqlite3
from langchain_core.tools import tool

@tool
def outlet_open_now(outlet_name: str) -> str:
    """Check if a given ZUS Coffee outlet is currently open based on its open and close time."""
    try:
        now = datetime.now().time()
        conn = sqlite3.connect("data/outlets.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT open_time, close_time FROM zus_outlets WHERE name LIKE ?",
            (f"%{outlet_name}%",)
        )
        result = cursor.fetchone()
        conn.close()

        if not result:
            return f"No outlet found with name matching '{outlet_name}'."

        open_str, close_str = result
        open_time = datetime.strptime(open_str.strip(), "%H:%M").time()
        close_time = datetime.strptime(close_str.strip(), "%H:%M").time()

        if open_time <= now <= close_time:
            return f"{outlet_name} is currently OPEN."
        else:
            return f"{outlet_name} is currently CLOSED."

    except Exception as e:
        return f"An error occurred while checking the outlet status: {str(e)}"

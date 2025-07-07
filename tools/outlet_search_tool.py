import sqlite3
from langchain_core.tools import tool

@tool
def outlet_lookup(location: str) -> str:
    """Search for ZUS Coffee outlets by name, address, city, or services."""
    conn = sqlite3.connect("data/outlets.db")
    cursor = conn.cursor()
    query = """
    SELECT name, address, city, services, open_time, close_time
    FROM zus_outlets
    WHERE name LIKE ? OR address LIKE ? OR city LIKE ? OR services LIKE ?
    """
    keyword = f"%{location}%"
    results = cursor.execute(query, (keyword, keyword, keyword, keyword)).fetchall()
    conn.close()

    if not results:
        return "No outlets found matching your query."

    return "\n\n".join([
        f"{r[0]} ({r[2]})\n{r[1]}\nServices: {r[3]}\nOpen: {r[4]} - {r[5]}"
        for r in results
    ])

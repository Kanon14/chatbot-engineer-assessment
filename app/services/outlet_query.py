import sqlite3

def search_outlet_db(location: str):
    conn = sqlite3.connect("data/outlets.db")
    cursor = conn.cursor()
    query = """
        SELECT shop_name, location, service, operating_hours 
        FROM zus_outlets 
        WHERE shop_name LIKE ? OR location LIKE ? OR service LIKE ?
    """
    like_query = f"%{location}%"
    results = cursor.execute(query, (like_query, like_query, like_query)).fetchall()
    conn.close()
    
    if not results:
        return "No outlets found."

    return [f"{r[0]} | {r[1]} | {r[2]} | Hours: {r[3]}" for r in results]

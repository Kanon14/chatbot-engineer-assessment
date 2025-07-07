import pandas as pd
import sqlite3

def create_outlet_db(csv_path: str, db_path: str):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("zus_outlets", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    print(f"[✓] SQLite DB created at {db_path}")
    
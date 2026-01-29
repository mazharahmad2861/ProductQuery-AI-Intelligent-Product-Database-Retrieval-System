import sqlite3

DB_PATH = "app/db/products.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def fetch_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_products_by_ids(ids):
    if not ids:
        return []
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM products WHERE id IN ({','.join(['?']*len(ids))})"
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    conn.close()
    return rows

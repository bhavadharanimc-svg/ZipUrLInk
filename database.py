import sqlite3
import hashlib

def get_connection():
    conn = sqlite3.connect("urls.db")
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            clicks INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def generate_short_code(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]

def save_url(original_url, short_code):
    conn = get_connection()
    conn.execute("INSERT OR IGNORE INTO urls (original_url, short_code) VALUES (?, ?)",
                 (original_url, short_code))
    conn.commit()
    conn.close()

def get_original_url(short_code):
    conn = get_connection()
    cursor = conn.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def increment_clicks(short_code):
    conn = get_connection()
    conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()
def get_all_urls():
    conn = get_connection()
    cursor = conn.execute("SELECT original_url, short_code, clicks FROM urls ORDER BY clicks DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
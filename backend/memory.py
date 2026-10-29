import sqlite3

def save_message(role, content):
    conn = sqlite3.connect("nahida.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        role TEXT NOT NULL,
        content TEXT NOT NULL
        )
    """)

    conn.execute("""
        INSERT INTO messages (role, content)
        VALUES (?, ?)
    """, (role, content))

    conn.commit()

    conn.close()

def load_messages():
    conn = sqlite3.connect("nahida.db")

    cursor = conn.execute("""
        SELECT role, content FROM messages
        ORDER BY id ASC
    """)

    messages = cursor.fetchall()
    conn.close()
    return messages

if __name__ == "__main__":
    save_message("user", "Mình đang học SQLite!")

if __name__ == "__main__":
    history = load_messages()
    print(history)
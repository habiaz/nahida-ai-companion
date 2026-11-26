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

def search_messages(keyword):
    conn = sqlite3.connect("nahida.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, content FROM messages WHERE content LIKE ?",
        ("%" + keyword + "%",)
    )

    messages = cursor.fetchall()

    conn.close()

    return messages

def retrieve_memories(message, limit=5):
    stopwords = {
        "what", "is", "my", "do", "you", "remember",
        "about", "the", "your", "are", "can",
        "có", "nhớ", "của", "tui", "là", "gì", "không",
        "hello", "hi", "hey", "nahida", "today", "how"
    }

    keywords = [
        word.strip(".,!?;:").lower()
        for word in message.split()
        if len(word.strip(".,!?;:")) >= 3
        and word.strip(".,!?;:").lower() not in stopwords
    ]

    candidates = []

    for keyword in keywords:
        for role, content in search_messages(keyword):
            item = (role, content)

            if role == "user" and item not in candidates:
                candidates.append(item)

    candidates.sort(
        key=lambda item: (
            sum(k in item[1].lower() for k in keywords),
            "?" not in item[1]
        ),
        reverse=True
    )

    return candidates[:limit]

if __name__ == "__main__":
    result = search_messages("SQLite")
    print(result)



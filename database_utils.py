import sqlite3
from datetime import datetime

# Create a connection to the SQLite database
def create_connection(db_file="mental_health_bot.db"):
    conn = sqlite3.connect(db_file)
    return conn

def create_table():
    conn = create_connection()
    # SQL query to create the chats table if it doesn't exist
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT,
        sender TEXT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()

def insert_chat(conversation_id, sender, message):
    conn = create_connection()
    # SQL query to insert a new chat record
    insert_sql = """
    INSERT INTO chats (conversation_id, sender, message, timestamp)
    VALUES (?, ?, ?, ?);
    """
    timestamp = datetime.now()  # Get current timestamp
    cursor = conn.cursor()
    cursor.execute(insert_sql, (conversation_id, sender, message, timestamp))
    conn.commit()
    conn.close()

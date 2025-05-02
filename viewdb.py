import sqlite3

def view_database(db_file="mental_health_bot.db"):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Query to fetch all records from the chats
        cursor.execute("SELECT * FROM chats")
        rows = cursor.fetchall()
        
        # Display the data
        if rows:
            print("\n=== Chat History ===")
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Sender: {row[2]}")
                print(f"Message: {row[3]}")
                print(f"Timestamp: {row[4]}")
                print("=" * 30)
        else:
            print("No records found in the database.")

        conn.close()
    
    except sqlite3.Error as e:
        print(f"Error reading database: {e}")

if __name__ == "__main__":
    view_database()
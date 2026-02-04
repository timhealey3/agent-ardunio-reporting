import sqlite3
'''
fetch data from Arduino board every 5 minutes, filling out a database
'''
def main():
    print("cron job ran")
    conn = sqlite3.connect("temperatures.db")
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS temps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    conn.commit()
    
    cursor.execute(
    "INSERT INTO temps (temperature) VALUES (?)",
    (getTemp(),)
)
    conn.commit()
    conn.close()

def getTemp():
    return 50.50

if __name__ == "__main__":
    main()

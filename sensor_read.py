import sqlite3
import serial
import time

ARDUINO_FAILED_CONNECT = "Failed to connect to the arduino"


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
    try:
        # Change to your actual port
        arduino = serial.Serial(port='/dev/tty.usbmodem1101', baudrate=9600, timeout=1)
        time.sleep(2) 
        data = arduino.readline().decode('utf-8').strip()
        arduino.close()
        return data
    except:
        raise ConnectionError(ARDUINO_FAILED_CONNECT)

if __name__ == "__main__":
    main()

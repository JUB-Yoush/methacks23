from flask import Flask,redirect,url_for, render_template
import no_gui_pomo
import sqlite3
import datetime

import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14501',9600)

# Create the Flask application object
app = Flask(__name__)

pomodoro  = no_gui_pomo.PomodoroTimer()

start_time = 0
end_time = 0

@app.route('/timer')
def timer():
    return render_template('timer.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    print('hahahah')
    ser.write(b'p')  # Send the command to start the timer
    ser.write(b's')  # Send the command to stop the timer
    pomodoro.start_timer()
    
@app.route('/')
def home():
    conn = sqlite3.connect('study_log.db')
    cur = conn.cursor()
    #cur.execute('SELECT * FROM tablename')

    start_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M")
    end_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M")
    tag = "math"
    num_sessions = 1

    # Define the SQL query
    query = """
        INSERT INTO study_sessions (start_date, end_date, tag, num_sessions)
        VALUES (?, ?, ?, ?)
    """
    # Execute the query
    cur.execute(query, (start_date, end_date, tag, num_sessions))
    cur.execute(query, (start_date, end_date, tag, num_sessions))

    cur.execute('SELECT * FROM study_sessions')
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
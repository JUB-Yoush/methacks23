from flask import Flask,redirect,url_for, render_template, request
import no_gui_pomo
import sqlite3
import datetime
import json
import test_json_write

#import serial
#import time

#ser = serial.Serial('/dev/cu.usbmodem14501',9600)

# Create the Flask application object
app = Flask(__name__)

#pomodoro  = no_gui_pomo.PomodoroTimer()

start_time = 0
end_time = 0

@app.route('/timer')
def timer():
    return render_template('timer.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    print('backend call worked')
    #ser.write(b'p')  # Send the command to start the timer
    #ser.write(b's')  # Send the command to stop the timer
#    pomodoro.start_timer()
    
@app.route('/')
def home():
    conn = sqlite3.connect('study_log.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM study_sessions')
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)


@app.route('/api/add_session',methods=['POST'])
def add_session(time_start,time_end,tag,pomodoro_count):

    time_start = request.json['time_start']
    time_end = request.json['time_end']
    tag = request.json['tag']
    pomodoro_count = request.json['pomodoro_count']

    conn = sqlite3.connect('study_log.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM study_sessions")
    query = """
        INSERT INTO study_sessions (start_date, end_date, tag, num_sessions)
        VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (start_time, end_time, tag, pomodoro_count))
    conn.close()

#def write_data():
    #cur.execute('SELECT * FROM study_sessions')
    #data = cur.fetchall()
    #conn.close()
    
    


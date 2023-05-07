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
    ser.write(b'p')  # Send the command to start the timer
    pass
    
@app.route('/')
def home():
    conn = sqlite3.connect('study_log.db')
    cur = conn.cursor()
    #cur.execute('SELECT * FROM tablename')

    start_date = datetime.datetime(2023, 4, 7, 14, 30, 0) 
    end_date = datetime.datetime(2023, 4, 7, 17, 30, 0) 
    start_date = start_date.strftime("%y-%m-%d %H:%M")
    end_date = end_date.strftime("%y-%m-%d %H:%M")
    tag = "math"
    num_sessions = 3

    # Define the SQL query
    query = """
        INSERT INTO study_sessions (start_date, end_date, tag, num_sessions)
        VALUES (?, ?, ?, ?)
    """
    # Execute the query
    cur.execute(query, (start_date, end_date, tag, num_sessions))

    start_date = datetime.datetime(2023, 4, 8, 10, 30, 0) 
    end_date = datetime.datetime(2023, 4, 8, 15, 30, 0) 
    start_date = start_date.strftime("%y-%m-%d %h:%m")
    end_date = end_date.strftime("%y-%m-%d %H:%M")
    tag = "history"
    num_sessions = 5

    cur.execute(query, (start_date, end_date, tag, num_sessions))

    start_date = datetime.datetime(2023, 4, 9, 12, 30, 0) 
    end_date = datetime.datetime(2023, 4, 9, 17, 30, 0) 
    start_date = start_date.strftime("%y-%m-%d %H:%M")
    end_date = end_date.strftime("%y-%m-%d %H:%M")
    tag = "work"
    num_sessions = 5

    cur.execute(query, (start_date, end_date, tag, num_sessions))

    cur.execute('SELECT * FROM study_sessions')
    data = cur.fetchall()
    c = cur
    c.execute("SELECT * FROM study_sessions ORDER BY id DESC LIMIT 1;")
    row = list(c.fetchall()[0])
    last_date = row[1]
    last_date = datetime.datetime.strptime(last_date,"%y-%m-%d %H:%M") #start
    last_date2 = row[2]
    last_date2 = datetime.datetime.strptime(last_date2,"%y-%m-%d %H:%M") #end
    
    #Find time elapsed after last session
    now = datetime.datetime.now()
    delta = now - last_date
    hours = (delta.seconds - delta.seconds%3600)/3600
    minutes = ( (delta.seconds - hours*3600) - (delta.seconds - hours*3600)%60 )/60
    seconds = delta.seconds - (minutes*60 + hours*3600)
    lastSessionString = f"{delta.days} days since last session"
    
    #Duration of last session
    delta = last_date2 - last_date
    hours = (delta.seconds - delta.seconds%3600)/3600
    minutes = ( (delta.seconds - hours*3600) - (delta.seconds - hours*3600)%60 )/60
    seconds = delta.seconds - (minutes*60 + hours*3600)
    durationString = f"Duration of last session: {hours} hours, {minutes} minutes, and {seconds} seconds"
    
    stats = {"duration": durationString, "lastSession": lastSessionString}
    
    conn.close()
    return render_template('index.html', data=data, stats=stats)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
from flask import Flask,redirect,url_for, render_template
import no_gui_pomo
import sqlite3
import datetime
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
    #START ARDUINO 
    pass
    
@app.route('/')
def home():
    conn = sqlite3.connect('study_log.db')
    cur = conn.cursor()
    #cur.execute('SELECT * FROM tablename')

    start_date = datetime.datetime(2023, 5, 7, 14, 30, 0) 
    end_date = datetime.datetime(2023, 5, 7, 17, 30, 0) 
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

    start_date = datetime.datetime(2023, 5, 8, 10, 30, 0) 
    end_date = datetime.datetime(2023, 5, 8, 15, 30, 0) 
    start_date = start_date.strftime("%y-%m-%d %h:%m")
    end_date = end_date.strftime("%y-%m-%d %H:%M")
    tag = "history"
    num_sessions = 5

    cur.execute(query, (start_date, end_date, tag, num_sessions))

    start_date = datetime.datetime(2023, 5, 8, 12, 30, 0) 
    end_date = datetime.datetime(2023, 5, 8, 17, 30, 0) 
    start_date = start_date.strftime("%y-%m-%d %H:%M")
    end_date = end_date.strftime("%y-%m-%d %H:%M")
    tag = "work"
    num_sessions = 5

    cur.execute(query, (start_date, end_date, tag, num_sessions))

    cur.execute('SELECT * FROM study_sessions')
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
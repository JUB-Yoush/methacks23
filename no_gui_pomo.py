import time
 
class PomodoroTimer:
    def __init__(self):
        self.time_left = 0
        self.running = False
        self.timer_text = ''

    def start_timer(self):
        self.running = True
        self.time_left = 50 * 60 * 1000
        self.update_timer_text()
        #self.start_button.config(state=tk.DISABLED)
        #self.stop_button.config(state=tk.NORMAL)
        #self.reset_button.config(state=tk.NORMAL)
        self.countdown()
 
    def stop_timer(self):
        self.running = False
        #self.start_button.config(state=tk.NORMAL)
        #self.stop_button.config(state=tk.DISABLED)
 
    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.update_timer_text()
        #self.start_button.config(state=tk.NORMAL)
        #self.stop_button.config(state=tk.DISABLED)
        #self.reset_button.config(state=tk.DISABLED)
 
    def countdown(self):
        while self.time_left > 0 and self.running:
            self.time_left -= 1
            self.update_timer_text()
            time.sleep(1)
        if self.running:
            self.running = False
            #self.start_button.config(state=tk.NORMAL)
            #self.stop_button.config(state=tk.DISABLED)
 
    def update_timer_text(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_text = f"{minutes:02d}:{seconds:02d}"
        print(self.timer_text,self.time_left)
 
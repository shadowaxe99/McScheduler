# This file will contain reminder functionality for the McScheduler project.

# Import necessary libraries
import time
import threading

# Define function to set a reminder

def set_reminder(reminder_time, message):
    current_time = time.time()
    delay = reminder_time - current_time
    if delay < 0:
        print('Reminder time is in the past.')
        return
    timer = threading.Timer(delay, lambda: print(message))
    timer.start()
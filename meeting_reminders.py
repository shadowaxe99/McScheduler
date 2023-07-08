# This file will contain meeting reminders functionality for the McScheduler project.

# Import necessary libraries
import datetime
import time

# Define function to set a reminder

def set_reminder(meeting_time):
    current_time = datetime.datetime.now()
    time_difference = meeting_time - current_time
    time_difference_in_seconds = time_difference.total_seconds()

    time.sleep(time_difference_in_seconds)

    print('Reminder: You have a meeting now.')
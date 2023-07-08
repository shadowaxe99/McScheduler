# This file will contain the dashboard for the McScheduler project.

# Import necessary libraries
import flask

# Define the dashboard route

@app.route('/dashboard')
def dashboard():
    return 'This is the dashboard.'
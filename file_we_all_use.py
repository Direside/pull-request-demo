"""
Sample Python App
"""

from flask import Flask

app = Flask(__name__)

# Main Route for the app
@app.route('/')
def index():
    return 'Hello World!'

# Signup page
@app.route('/signup')
def signup():
    return 'Please create an account here.'

"""
Sample Python App
"""

from flask import Flask

app = Flask(__name__)

"""
Main method for app
"""
@app.route('/')
def index():
    return 'Hello World!'

"""
Signup Page
"""
@app.route('/signup')
def signup():
    return 'Please create an account here.'

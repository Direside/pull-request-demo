"""
Sample Python App
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main method for app"""
    return 'Hello World!'

@app.route('/signup')
def signup():
    """Signup Page"""
    return 'Please create an account here.'

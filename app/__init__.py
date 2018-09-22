### Initialize the Flask application ###

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import environment variables from .env file that you don't want public
# e.g. secret keys, usernames, passwords
if os.path.exists('.env'):
    print('Importing environment from .env file')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

# Create database
db = SQLAlchemy()

# Initialize the application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Configure the application with database information
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Import the views/routes
from . import views

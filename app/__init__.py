"""
Initialize the Flask application
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create database
db = SQLAlchemy()

# Initialize the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

# Configure the application with database information
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Import the views/routes
from . import views

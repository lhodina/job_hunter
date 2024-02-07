from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = 'silent assassin, suit only'
CORS(app, supports_credentials=True)

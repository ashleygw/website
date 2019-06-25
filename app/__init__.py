from flask import Flask
import sys
print(sys.path)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
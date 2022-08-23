import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from config import DevelopementConfig, ProductionConfig

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or DevelopementConfig)

# инициализирует расширения
toolbar = DebugToolbarExtension(app)
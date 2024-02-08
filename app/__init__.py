from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")  # Importando configurações

db = SQLAlchemy(app)
# Importe os modelos depois de inicializar o db
from app import models

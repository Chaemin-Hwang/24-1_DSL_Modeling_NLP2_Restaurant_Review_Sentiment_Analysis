from flask import Flask
from flask import request, session, redirect, url_for, flash, json
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
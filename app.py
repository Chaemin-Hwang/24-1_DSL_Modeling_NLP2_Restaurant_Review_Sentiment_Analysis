from flask import Flask, render_template
from flask import request, session, redirect, url_for, flash, json
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


# 메인 페이지 라우트
@app.route('/')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

app.run()
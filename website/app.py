from flask import Flask, render_template
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


# 메인 페이지 라우트
@app.route('/')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/review_page_정통집')
def review_page_정통집():
    return render_template('review_page_정통집.html')

@app.route('/review_page_쭈꾸미')
def review_page_쭈꾸미():
    return render_template('review_page_쭈꾸미.html')

@app.route('/review_moa_정통집')
def review_moa_정통집():
    return render_template('review_moa_정통집.html')

@app.route('/review_moa_쭈꾸미')
def review_moa_쭈꾸미():
    return render_template('review_moa_쭈꾸미.html')

if __name__ == '__main__':
    app.run(debug=True)

app.run()
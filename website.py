from flask import Flask, url_for,render_template
app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/random')
def random():
    return render_template('random.html')

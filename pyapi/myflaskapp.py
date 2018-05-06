from flask import Flask

app = Flask(__name__)

@app.route('/pyapi')
def pyapi():
    return "<span style='color:red'>I am a Flask app!</span>"

@app.route('/pyapi/')
def index():
    return "<h1>Finally got this proxy shit working right!</h1><br/><p><a href='/'>Back home</a>"

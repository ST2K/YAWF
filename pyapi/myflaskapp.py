from flask import Flask

app = Flask(__name__)

@app.route('/pyapi/')
def pyapi():
    return "<span style='color:red'>I am a Flask app!</span>"


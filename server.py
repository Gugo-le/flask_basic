from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

app.run(port = 5000, debug=True)

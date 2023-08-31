from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read' +id

app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pw@localhost:3306/songtest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
# Create SQLAlchemy object
db = SQLAlchemy(app)

class Song(db.Model):
    __tablename__ = 'songtest'  

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    album = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    song_list = Song.query.all()
    return render_template('index.html', song_list=song_list)

if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드를 활성화하여 개발 중에 디버깅을 수행합니다.

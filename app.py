from flask import Flask
from database import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
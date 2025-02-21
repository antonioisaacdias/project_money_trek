from flask import Flask
from flask_login import LoginManager
from app.database import db
from app.config import Config
from app.models.user import User 
from app.routes.views.home import home_bp

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(home_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run(debug=True)
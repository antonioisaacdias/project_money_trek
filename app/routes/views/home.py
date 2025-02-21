from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, template_folder='app/templates')

@home_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@home_bp.route('/solicite', methods=['GET'])
def proposal():
    return render_template('proposal.html')

@home_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@home_bp.route('/recuperar-senha', methods=['GET'])
def recover_password():
    return render_template('recover-password.html')

@home_bp.route('/quem-somos', methods=['GET'])
def about_us():
    return render_template('about-us.html')

from flask import Config, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from loangenie import candidates
from loangenie.configure import Config



login_manager = LoginManager()
login_manager.login_view = 'users.login'
bcrypt = Bcrypt()
db = SQLAlchemy()
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from loangenie.users.routes import users
    from loangenie.main.routes import main
    from loangenie.candidates.routes import candidates
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(candidates)

    return app



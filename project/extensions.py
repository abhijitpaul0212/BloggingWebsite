from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

# Create a ORM
db = SQLAlchemy()

# Login Manager
login_manager = LoginManager()

# Mail
mail = Mail()
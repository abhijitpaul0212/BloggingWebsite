from dotenv import load_dotenv

from flask import Flask
from config import DevelopmentConfig

from project.routes.main import bp as main_bp
from project.routes.users import bp as users_bp
from project.routes.blogs import bp as blogs_bp
from project.extensions import db, login_manager, mail
from project.models.blog import CategoryMaster

from project.routes.blogs.routes import get_all_categories

from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user, login_user, logout_user

load_dotenv()

def create_app(config_class=DevelopmentConfig):
    """Application-Factory pattern

    Args:
        config_class (Config): Config 
    """
    # Create flask instance
    app = Flask(__name__)
    app.secret_key = 'zjHUlXmuO85d2LOHqbzpd8_Qvv0XhUYxDr0ZRg2UG04'
    app.config.from_object(config_class)
    
    # extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    login_manager.login_view = 'users.login'
    
    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(blogs_bp)

    # push context manually to app
    with app.app_context():
        db.create_all()  # Handling prerequisite of creating all tables 
        get_all_categories()
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

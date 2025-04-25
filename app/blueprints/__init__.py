from .staff import user_bp
from .register import bp as register_bp

def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(register_bp)

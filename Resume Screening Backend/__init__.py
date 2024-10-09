
from flask import Flask
from flask_cors import CORS
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.register_blueprint(main)

    # Print the list of registered routes
    with app.app_context():
        print("Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint}: {rule}")

    return app



import os, werkzeug
from flask import Flask, render_template, redirect, request, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # home page
    @app.route("/")
    def startup():
        return render_template('index.html')
    
    @app.route("/404")
    def error_page():
        return render_template('404.html')
    
    @app.route("/pasta")
    def pasta():
        return render_template('pasta.html')

    @app.route("/pizza")
    def pizza():
        return render_template('pizza.html')
        
    @app.route("/lasagna")
    def lasagna():
        return render_template('lasagna.html')
    

    return app

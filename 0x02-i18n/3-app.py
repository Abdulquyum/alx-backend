#!/usr/bin/env python3
""" Translate with Babel """


from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get location lang """
    return request.accept_languages.best_match(["en", "fr"])

@app.route('/', strict_slashes=False)
def greetings():
    """ render a simple html """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

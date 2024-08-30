#!/usr/bin/env python3
"""
Basic Flask app with Babel for timezone and location
"""

from flask import Flask, render_template, request
from babel import Babel, localeselector


app = Flask(__name__)


class Config:
    """ Set langauge and zone """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """ Select best match language """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/', strict_slashes=False)
def basic():
    """ render root path """
    return render_template('2-index.html')


if __name__ == '__main__':
    """ Run app """
    app.run(host='0.0.0.0', port=5000)

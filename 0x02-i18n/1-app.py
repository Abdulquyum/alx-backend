#!/usr/bin/python3
""" Simple flask app rendering an html page """


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ configuration of language and tiemzone """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

@app.route('/', strict_slashes=False)
def basic_babel():
    """ basic testing root func """
    return render_template('1-index.html')

if __name__ == '__main__':
    """ Run """
    app.run(host='0.0.0.0', port=5000)

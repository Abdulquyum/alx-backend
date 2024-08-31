#!/usr/bin/env python3
""" Translate with Babel """


from flask import Flask, request, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }

class Config:
    """ Configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_user():
    login_as = request.args.get('login_as')

    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id, None)
        except ValueError:
            return None

    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ get location lang """
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def greetings():
    """ render a simple html """
    return render_template('5-index.html')

if __name__ == '__main__':
    """ Run App """
    app.run(host='0.0.0.0', port=5000)

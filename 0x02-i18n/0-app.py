#!/usr/bin/env python3
""" Simple flask app rendering an html page """


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def basic():
    """route destination """
    return render_template('0-index.html')

if __name__ == '__main__':
    """ Run """
    app.run(host='0.0.0.0', port=5000)

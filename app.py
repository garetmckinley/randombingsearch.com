import os
import tortilla
from flask import Flask, render_template
from flask.ext.classy import FlaskView

# Create our Flask app
app = Flask(__name__)

# Fetch the secret key from our environment
app.secret_key = os.environ.get("SECRET_KEY")


def Question():
    # Wrap the jService API
    jService = tortilla.wrap('http://jservice.io/api')
    # Fetch a random trivia question from the jService.io API
    try:
        response = jService.random.get(params={'count': 1})[0]
    except Exception as e:
        return False
    # Retreive only the question from the response object
    question = response['question']
    return question


def BingBackground():
    # Wrap the Bing HPImageArchive API
    HPImageArchive = tortilla.wrap('http://www.bing.com/HPImageArchive.aspx')
    response = HPImageArchive.get(params={
        'format': 'js',
        'idx': 0,
        'n': 1,
        'mkt': 'en-US'
    })
    image = 'http://bing.com/%s' % response['images'][0]['url']
    return image


# This is the class for the home page view
class AppView(FlaskView):
    # Route this view to the root '/' of our url
    route_base = '/'

    # This is the function that renders the home page
    def index(self):
        return render_template('index.html', background=BingBackground())
# Register the view with our app
AppView.register(app)


# This is the class for the /search/ view.
class SearchView(FlaskView):
    # This is the function that renders the /search/ page
    def index(self):
        # Return the redirect template with the question passed to it
        return render_template('redirect.html', question=Question())
# Register the view with our app
SearchView.register(app)

# If this file is being run and not imported
if __name__ == '__main__':
    # Enable debug mode (disable in production)
    app.debug = True
    # Run our Flask app
    app.run()

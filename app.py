from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)




@app.get('/')
def get_homepage():
    """Return homepage and show questions form"""

    silly_prompts = silly_story.prompts

    return render_template("questions.html", prompts = silly_prompts )


@app.get('/results')
def get_results():
    """Return results page with results from questions"""

    silly_story = silly_story.template
    silly_answers = request.args[f"silly_prompts"]

    return render_template("results.html", story = silly_story, )

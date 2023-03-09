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

    # silly_template = silly_story.template
    test_answers = {"place": "New York", "noun": "person", "verb": "run",
                    "adjective": "greasy", "plural_noun": "computers"}
    # silly_answers = request.args[silly_story.prompts]
    completed_story = silly_story.generate(test_answers)


    return render_template("results.html",
                            story = completed_story )

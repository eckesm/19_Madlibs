from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import sample
import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_02-12-2021_14-22-44'
debug = DebugToolbarExtension(app)


@app.route('/')
def show_story_selection():
    stories_list = stories.STORIES
    return render_template('story_selection.html', stories=stories_list)


@app.route('/form')
def show_form():
    story_id = request.args['story']
    story = stories.dict_stories_by_id[story_id]
    
    prompts = story.prompts
    randomized_prompts = sample(prompts, len(prompts))
    
    return render_template('form.html', prompts=randomized_prompts, story=story)


@app.route('/story')
def show_story():
    story_id = request.args['story']
    story = stories.dict_stories_by_id[story_id]
    
    answers = dict(request.args)
    completed_story = story.generate(answers)

    return render_template('story.html', completed_story=completed_story, answers=answers)

from flask import Blueprint, render_template

temp_view = Blueprint('temp_view', __name__)

@temp_view.route("/")
def index():
    return render_template('index.html', varr='6')
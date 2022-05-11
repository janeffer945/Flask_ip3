from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import  User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
from ..models import Pitch, User, Comment, Upvote, Downvote

from .forms import UpdateProfile,PitchForm,CommentForm,UpvoteForm
# from .forms import UpdateProfile,PitchForm,CommentForm
@main.route('/')
def index():
    pitches = Pitch.query.all()
    interview = Pitch.query.filter_by(category = 'Interview').all() 
    product = Pitch.query.filter_by(category = 'Product').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()

    return render_template('index.html', interview = interview,product = product, pitches = pitches,promotion= promotion)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

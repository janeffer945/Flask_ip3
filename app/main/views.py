from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import  User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
from ..models import Pitch, User, Comment, Upvote, Downvote

from .forms import UpdateProfile,PitchForm,CommentForm,UpvoteForm
# from .forms import UpdateProfile,PitchForm,CommentForm
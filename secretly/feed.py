from flask import Blueprint, render_template, request, redirect, url_for

from .models.feed import Record, Like, Comment, CommentLike
from .db import db
from .forms.feed import PostForm, CommentForm

feed = Blueprint('feed', __name__, template_folder='templates')


@feed.route('/')
def index():
    return render_template('feed.html', feed=Record.query.all()[0:10])


@feed.route('/like/<record_id>')
def like(record_id):
    if Like.query.filter_by(record_id=record_id, owner_id=request.user.id).count():
        return redirect('/')
    like = Like(record_id=record_id, owner_id=request.user.id)
    db.session.add(like)
    db.session.commit()
    return redirect('/')


@feed.route('/comment_like/<comment_id>')
def comment_like(comment_id):
    comment = Comment.query.get(comment_id)
    redirect_url = url_for('.comments', record_id=comment.record.id)
    if CommentLike.query.filter_by(comment_id=comment_id, owner_id=request.user.id).count():
        return redirect(redirect_url)
    like = CommentLike(comment_id=comment_id, owner_id=request.user.id)
    db.session.add(like)
    db.session.commit()
    return redirect(redirect_url)


@feed.route('/comments/<record_id>')
def comments(record_id):
    record = Record.query.get(record_id)
    comments = Comment.query.filter_by(record_id=record_id)
    return render_template('comments.html', comments=comments, record=record)


@feed.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        record = Record(text=form.text.data, owner_id=request.user.id)
        db.session.add(record)
        db.session.commit()
        return redirect('/')
    return render_template('post.html', form=form)


@feed.route('/new_comment/<record_id>', methods=['GET', 'POST'])
def new_comment(record_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, record_id=record_id, owner_id=request.user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.comments', record_id=record_id))
    return render_template('new_comment.html', form=form)

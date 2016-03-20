from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, UniqueConstraint
from ..db import db
import datetime


class Record(db.Model):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('users.id'))
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now())

    comments = db.relationship('Comment', backref='record')
    likes = db.relationship('Like', backref='record')

    @property
    def like_count(self):
        return Like.query.filter_by(record_id=self.id).count()

    @property
    def comment_count(self):
        return Comment.query.filter_by(record_id=self.id).count() or 0


class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    record_id = Column(ForeignKey('records.id'))
    owner_id = Column(ForeignKey('users.id'))
    text = Column(Text)
    likes = db.relationship('CommentLike', backref='comment')

    @property
    def like_count(self):
        return CommentLike.query.filter_by(comment_id=self.id).count()


class Like(db.Model):
    __tablename__ = 'likes'
    __table_args__ = (
        UniqueConstraint('record_id', 'owner_id'),)
    id = Column(Integer, primary_key=True)
    record_id = Column(ForeignKey('records.id'))
    owner_id = Column(ForeignKey('users.id'))


class CommentLike(db.Model):
    __tablename__ = 'comment_likes'
    __table_args__ = (
        UniqueConstraint('comment_id', 'owner_id'),)
    id = Column(Integer, primary_key=True)
    comment_id = Column(ForeignKey('comments.id'))
    owner_id = Column(ForeignKey('users.id'))

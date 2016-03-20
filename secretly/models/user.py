from sqlalchemy import Column, Integer, String
from ..db import db
import hashlib


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    salt = Column(String(255))
    comments = db.relationship('Comment', backref='owner')
    likes = db.relationship('Like', backref='owner')

    @property
    def avatar(self):
        m = hashlib.md5()
        m.update(self.salt.encode('utf-8'))
        return 'http://www.gravatar.com/avatar/%s?d=monsterid' % m.hexdigest()

from sqlalchemy import Column, Integer, ForeignKey, String
from ..db import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(255))

class Record(db.Model):
    __tablename__ = 'records'
    id = Column(Integer, primary_key = True)
    owner_id = Column(ForeignKey('users.id'))

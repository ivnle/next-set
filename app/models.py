from datetime import datetime
from app import db, ma


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.String)

    def __repr__(self):
        return '<Post {}>'.format(self.name)


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
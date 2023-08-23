from project.extensions import db
from enum import unique

class BlogModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_master.category_id'), nullable=False)
    blog_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    blog_text = db.Column(db.Text, nullable=False)
    blog_creation_date = db.Column(db.DateTime)
    blog_read_count = db.Column(db.Integer, default=0)
    blog_rating_count = db.Column(db.Integer, default=0)
    
class CategoryMaster(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, nullable=False, unique=True)
    blogmodel = db.relationship('BlogModel', backref='categorymaster', lazy=True)
    
class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog_model.id'), nullable=True)
    blog_comment = db.Column(db.Text)
    comment_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    blog_rating = db.Column(db.Integer)
    blog_comment_date = db.Column(db.DateTime)
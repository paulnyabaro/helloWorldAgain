# from flask import Flask, request, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     grade = db.Column(db.String(20), nullable=True)
# def __repr__(self):
#     return '<Student %r>' % self.name

# Error handling
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('error404.html'), 404
# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('error500.html'), 500

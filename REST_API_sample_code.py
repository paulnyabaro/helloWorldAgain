# Representational State Transfer

# Working with RESTful in flask
# pip install Flask-RESTful
#
# Fetching and deleting data from db
# class StudentDao(Resource):
#     def get(self, student_id):
#         student = Student.query.filter_by(id=student_id).first_or_404(description='Record with id={} is not available'.format(student_id))
#     return student.serialize()
#     def delete(self, student_id):
#         student = Student.query.filter_by(id=student_id).first_or_404(description='Record with id={} is not available'.format(student_id))
#     db.session.delete(student)
#     db.session.commit()
#     return '', 204
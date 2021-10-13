from flask import Flask , render_template, request, redirect, url_for, flash, jsonify
# from wtforms import IntegerField, StringField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import Form
# from wtforms import StringField, IntegerField , validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regNum = db.Column(db.String(20),  nullable=False)
    quiz1 = db.Column(db.Integer, nullable=False)
    quiz2 = db.Column(db.Integer, nullable=False)
    midTerm = db.Column(db.Integer, nullable=False)
    exam = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Student' + str(self.id)




@app.route('/')
def index():
    # get all students from database
    students = Student.query.all()
    return  render_template('index.html' , students=students)

@app.route('/form' , methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        regNum = int(request.form['regNum'])
        quiz1 = int(request.form['quiz1'])
        quiz2 = int(request.form['quiz2'])
        midTerm = int(request.form['midTerm'])
        exam = int(request.form['exam'])
        total = quiz1 + quiz2 + midTerm + exam
        student = Student(regNum=regNum, quiz1=quiz1, quiz2=quiz2, midTerm=midTerm, exam=exam, total=total)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('index'))
    return render_template('form.html')




if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)



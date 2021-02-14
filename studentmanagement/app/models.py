from app import db

class Major(db.Model):
    __tablename__ = "major"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50))
    students = db.relationship('Student', backref = 'student', lazy = True)
    professor = db.relationship('Professor', backref = 'professor', lazy = True)
    lectures = db.relationship('Lecture', backref = 'lecture', lazy = True)


class Student(db.Model):
    __tablename__ = "student"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(20))
    birth = db.Column(db.Date)
    phone = db.Column(db.String(30))
    email = db.Column(db.String(50))
    major = db.Column(db.Integer, db.ForeignKey('major.id'))
    admission_date = db.Column(db.Date)
    semester = db.Column(db.Integer)

    lecStudent = db.relationship('LectureStudent', backref = 'lecture', lazy = True)


class Professor(db.Model):
    __tablename__ = "professor"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(20))
    birth = db.Column(db.Date)
    phone = db.Column(db.String(30))
    email = db.Column(db.String(50))
    major = db.Column(db.Integer, db.ForeignKey('major.id'))

    lectures = db.relationship('Lecture', backref = 'lecture', lazy = True)


class Lecture(db.Model):
    __tablename__ = "lecture"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    opened_grade = db.Column(db.Integer)
    grades = db.Column(db.Integer)
    major = db.Column(db.Integer, db.ForeignKey('major.id'))
    professor = db.Column(db.Integer, db.ForeignKey('professor.id'))
    place = db.Column(db.String(50))

    times = db.relationship('LectureTime', backref = 'lecture', lazy = True)
    lecStudent = db.relationship('LectureStudent', backref = 'lecture', lazy = True)

class LectureTime(db.Model):
    __tablename__ = "lecture_time"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    lecture = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    time = db.Column(db.DateTime)


class LectureStudent(db.Model):
    __tablename__ = "lecture_student"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.Integer, db.ForeignKey('student.id'))
    lecture = db.Column(db.Integer, db.ForeignKey('lecture.id'))

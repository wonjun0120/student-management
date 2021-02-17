from app import db

class Major(db.Model):
    __tablename__ = "major"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50))
    students = db.relationship('Student', lazy = True)
    professor = db.relationship('Professor', lazy = True)
    lectures = db.relationship('Lecture', lazy = True)

    def __init__(self, full_name):
        self.full_name = full_name

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

    lecStudent = db.relationship('LectureStudent', lazy = True)

    def __init__(self, full_name, birth, phone, email, admission_date, semester):
        self.full_name = full_name
        self.birth = birth
        self.phone = phone
        self.email = email
        self.admission_date = admission_date
        self.semester = semester

class Professor(db.Model):
    __tablename__ = "professor"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(20))
    birth = db.Column(db.Date)
    phone = db.Column(db.String(30))
    email = db.Column(db.String(50))
    major = db.Column(db.Integer, db.ForeignKey('major.id'))

    lectures = db.relationship('Lecture', lazy = True)

    def __init__(self, full_name, birth, phone, email):
        self.full_name = full_name
        self.birth = birth
        self.phone = phone
        self.email = email


class Lecture(db.Model):
    __tablename__ = "lecture"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(20))
    major = db.Column(db.Integer, db.ForeignKey('major.id'))
    professor = db.Column(db.Integer, db.ForeignKey('professor.id'))
    place = db.Column(db.String(50))

    lecStudent = db.relationship('LectureStudent', lazy = True)

    def __init__(self, full_name, place):
        self.full_name = full_name
        self.place = place

class LectureStudent(db.Model):
    __tablename__ = "lecture_student"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.Integer, db.ForeignKey('student.id'))
    lecture = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    grade = db.Column(db.String(10))

    def __init__(self, grade):
        self.grade = grade
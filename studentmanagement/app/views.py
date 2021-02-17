from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import Student, Professor, Lecture, Major, LectureStudent

@app.route('/')
def main_page():
    return render_template('index.jinja2')

@app.route('/major', methods= ['GET', 'POST'])
def major():
    if request.method == 'POST':
        # print(request.form)
        new_major = Major(request.form['full_name'])
        db.session.add(new_major)
        db.session.commit()
    majors = Major.query.all()
    return render_template('major.jinja2', major=majors)

@app.route("/delMajor/<id>")
def delMajor(id):
    maj = Major.query.get(id)
    db.session.delete(maj)
    db.session.commit()

    majors = Major.query.all()
    return render_template('major.jinja2', major=majors)

@app.route("/getmajor/<id>")
def getmajor(id):
    major = Major.query.get(id)

    join_prof = db.session.query(Professor, Major).\
        filter(Professor.major == Major.id).\
        filter(Major.id == id).\
        all()
        
    students = db.session.query(Student, Major).\
        filter(Student.major == Major.id).\
        filter(Major.id == id).all()

    lectures = db.session.query(Lecture, Major).\
        filter(Lecture.major == Major.id).\
        filter(Major.id == id).all()
        
    return render_template('majorPop.jinja2', major=major, professors=join_prof, students=students, lectures=lectures)

@app.route("/editMajor/<id>", methods=['POST', 'GET'])
def editMajor(id):
    major = Major.query.get(id)

    if request.method == 'POST':
        major.full_name = request.form['full_name']
        db.session.commit()
        
    join_prof = db.session.query(Professor, Major).\
        filter(Professor.major == Major.id).\
        filter(Major.id == id).\
        all()
        
    students = db.session.query(Student, Major).\
        filter(Student.major == Major.id).\
        filter(Major.id == id).all()

    lectures = db.session.query(Lecture, Major).\
        filter(Lecture.major == Major.id).\
        filter(Major.id == id).all()
        
    return render_template('majorPop.jinja2', major=major, professors=join_prof, students=students, lectures=lectures)

@app.route("/professor", methods= ['GET', 'POST'])
def professor():
    if request.method == 'POST':
        # print(request.form)
        maj = Major.query.get(request.form['major'])
        prof = Professor(request.form['full_name'], request.form['birth'], request.form['phone'], request.form['email'])
        prof.major = maj.id
        db.session.add(prof)
        db.session.commit()

    join_prof = db.session.query(Professor, Major).\
        filter(Professor.major == Major.id).all()

    majors = Major.query.all()
    return render_template('professor.jinja2', majors=majors, professors=join_prof)

@app.route("/delProf/<id>")
def delProf(id):
    prof = Professor.query.get(id)
    db.session.delete(prof)
    db.session.commit()

    join_prof = db.session.query(Professor, Major).\
        filter(Professor.major == Major.id).all()

    majors = Major.query.all()
    return render_template('professor.jinja2', majors=majors, professors=join_prof)

@app.route("/getProf/<id>")
def getProf(id):
    prof = Professor.query.get(id)
    lectures = db.session.query(Lecture, Professor).\
        filter(Lecture.professor == Professor.id).\
        filter(Professor.id == id).all()
    majors = Major.query.all()
    maj = Major.query.get(prof.major)
    return render_template('professorPop.jinja2', professor=prof, lectures=lectures, majors=majors, major=maj)


@app.route("/editProf/<id>", methods=['POST', 'GET'])
def editProf(id):
    prof = Professor.query.get(id)
    if request.method == 'POST':
        maj = Major.query.get(request.form['major'])
        prof.full_name = request.form['full_name']
        prof.birth = request.form['birth']
        prof.phone = request.form['phone']
        prof.email = request.form['email']
        prof.major = maj.id
        db.session.commit()
        
    professor = Professor.query.get(id)
    lectures = db.session.query(Lecture, Professor).\
        filter(Lecture.professor == Professor.id).\
        filter(Professor.id == id).all()
    majors = Major.query.all()
    maj = Major.query.get(prof.major)
    return render_template('professorPop.jinja2', professor=prof, lectures=lectures, majors=majors, major=maj)


@app.route("/student", methods= ['GET', 'POST'])
def student():
    if request.method == 'POST':
        # print(request.form)
        maj = Major.query.get(request.form['major'])
        stud = Student(
            full_name=request.form['full_name'], 
            birth=request.form['birth'], 
            phone=request.form['phone'], 
            email=request.form['email'], 
            admission_date=request.form['admission_date'], 
            semester=request.form['semester']
        )
        stud.major = maj.id
        db.session.add(stud)
        db.session.commit()
    
    students = db.session.query(Student, Major).\
        filter(Student.major == Major.id).all()
    majors = Major.query.all()
    return render_template('student.jinja2', majors=majors, students=students)

@app.route("/delStud/<id>")
def delStud(id):
    stud = Student.query.get(id)
    db.session.delete(stud)
    db.session.commit()

    students = db.session.query(Student, Major).\
        filter(Student.major == Major.id).all()

    majors = Major.query.all()
    return render_template('student.jinja2', majors=majors, students=students)


@app.route("/getStud/<id>")
def getStud(id):
    stud = Student.query.get(id)
    majors = Major.query.all()
    maj = Major.query.get(stud.major)
    lectures = db.session.query(Lecture).\
        filter(Lecture.major == stud.major).all()
    lec_std = db.session.query(LectureStudent, Lecture).\
        filter(LectureStudent.student == id).\
        filter(LectureStudent.lecture == Lecture.id).all()
    print(lec_std)
    return render_template('studentPop.jinja2', student=stud, majors=majors, major=maj, lectures=lectures, lec_std=lec_std)

@app.route("/editStud/<id>", methods=['POST', 'GET'])
def editStud(id):
    stud = Student.query.get(id)
    if request.method == 'POST':
        maj = Major.query.get(request.form['major'])
        stud.full_name = request.form['full_name']
        stud.birth = request.form['birth']
        stud.phone = request.form['phone']
        stud.email = request.form['email']
        stud.admission_date = request.form['admission_date']
        stud.semester = request.form['semester']
        stud.major = maj.id
        db.session.commit()
        
    return redirect(url_for('getStud', id=id)) 


@app.route('/addLec2Stud/<id>', methods=["POST"])
def addLec2Stud(id):
    isExist = db.session.query(LectureStudent).filter(LectureStudent.student == id).filter(LectureStudent.lecture == request.form['lectures']).all()
    if request.method == 'POST' and not isExist:
        lec = Lecture.query.get(request.form['lectures'])
        stud = Student.query.get(id)
        lec_stud = LectureStudent(
            grade=request.form['grade']
        )

        lec_stud.lecture = lec.id
        lec_stud.student = stud.id
        db.session.add(lec_stud)
        db.session.commit()
    return redirect(url_for('getStud', id=id)) 

@app.route('/delLec2Stud/<id>')
def delLec2Stud(id):
    l2s = LectureStudent.query.get(id)
    studid = l2s.student
    db.session.delete(l2s)
    db.session.commit()

    return redirect(url_for('getStud', id=studid)) 

@app.route('/changeGrade/<id>', methods=['POST'])
def changeGrade(id):
    l2s = LectureStudent.query.get(id)
    studid = l2s.student
    if request.method == 'POST':
        l2s.grade = request.form["grade"]
        db.session.commit()
    return redirect(url_for('getStud', id=studid)) 

@app.route("/lecture", methods= ['GET', 'POST'])
def lecture():
    if request.method == 'POST':
        print(request.form)
        maj = Major.query.get(request.form['major'])
        prof = Professor.query.get(request.form['professor'])
        lec = Lecture(
            full_name = request.form['full_name'],
            place = request.form['place']
        )
        lec.major = maj.id
        lec.professor = prof.id
        db.session.add(lec)
        db.session.commit()


    majors = Major.query.all()
    professors = Professor.query.all()
    lectures = db.session.query(Lecture, Major, Professor).\
        filter(Major.id == Lecture.major).\
        filter(Professor.id == Lecture.professor).all()
    print(lectures)
    return render_template('lecture.jinja2',majors=majors, professors=professors, lectures=lectures)

@app.route("/delLec/<id>")
def delLec(id):
    lec = Lecture.query.get(id)
    db.session.delete(lec)
    db.session.commit()
    return redirect(url_for('lecture')) 

@app.route('/getLec/<id>')
def getLec(id):
    lec = Lecture.query.get(id)
    prof = Professor.query.get(lec.professor)
    maj = Major.query.get(lec.major)
    majors = Major.query.all()
    professors = Professor.query.all()
    students = db.session.query(Student, LectureStudent, Lecture).\
        filter(Student.id == LectureStudent.student).\
        filter(Lecture.id == LectureStudent.lecture).\
        filter(LectureStudent.lecture == id).all()
    maj_students = db.session.query(Student, Major).\
        filter(Major.id == Student.major).\
        filter(Major.id == lec.major).all()
    return render_template('lecturePop.jinja2', lecture=lec, major=maj, professor=prof, professors=professors, majors=majors, students=students, maj_students=maj_students)

@app.route('/editLec/<id>', methods= ['POST'])
def editLec(id):
    lec = Lecture.query.get(id)
    prof = Professor.query.get(request.form['professor'])
    maj = Major.query.get(request.form['major'])

    lec.full_name = request.form['full_name']
    lec.major = maj.id
    lec.professor = prof.id
    lec.place = request.form['place']
    db.session.commit()

    return redirect(url_for('getLec', id=id)) 


@app.route('/addStud2Lec/<id>', methods=["POST"])
def addStud2Lec(id):
    if request.method == 'POST':
        # print(request.form.getlist('students'))
        
        for s in request.form.getlist('students'):
            lec = Lecture.query.get(id)
            stud = Student.query.get(s)
            lec_stud = LectureStudent(
                grade=""
            )

            lec_stud.lecture = lec.id
            lec_stud.student = stud.id
            db.session.add(lec_stud)
            db.session.commit()

    return redirect(url_for('getLec', id=id)) 

@app.route('/delStud2Lec/<id>')
def delStud2Lec(id):
    l2s = LectureStudent.query.get(id)
    lecid = l2s.lecture
    db.session.delete(l2s)
    db.session.commit()

    return redirect(url_for('getLec', id=lecid)) 

@app.route('/changeGradeinLec/<id>', methods=['POST'])
def changeGradeinLec(id):
    l2s = LectureStudent.query.get(id)
    lecid = l2s.lecture
    if request.method == 'POST':
        l2s.grade = request.form["grade"]
        db.session.commit()
    return redirect(url_for('getLec', id=lecid)) 
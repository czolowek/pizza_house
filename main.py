from flask import Flask, render_template, request, redirect

from app.db.base import create_db, Session
from app.db.models import Pizza, Student, Group


app = Flask(__name__, template_folder="app/templates")


@app.get("/")
def index():
    with Session() as session:
        students = session.query(Student).all()
        return render_template("index.html", students=students)


@app.route("/add_student/", methods=["GET", "POST"])
def add_student():
    with Session() as session:
        groups = session.query(Group).all()

        if request.method == "POST":
            name = request.form.get("name")
            group_id = request.form.get("group_id")
            student = Student(name=name, group_id=group_id)
            session.add(student)
            session.commit()
            return redirect("/")

        return render_template("add_student.html", groups=groups)


@app.route("/add_group/", methods=["GET", "POST"])
def add_group():
    if request.method == "POST":
        with Session() as session:
            name = request.form.get("name")
            group = Group(name=name)
            session.add(group)
            session.commit()
            return redirect("/")

    return render_template("add_group.html")

if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=5000)




from flask import Blueprint, render_template
import COVID19Map.db.studentaction as stse

emp = Blueprint("emp", __name__)


@emp.route("/emp/studentsearch")
def searchstudent():
    list = stse.search_student()
    return render_template("student.html", list=list)

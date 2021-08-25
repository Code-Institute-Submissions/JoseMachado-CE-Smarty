import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get_employees")
def get_employees():
    employees = list(mongo.db.employees.find())
    return render_template("employees.html", employees=employees)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})


        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password", "danger")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session['user']:
        jobs = list(mongo.db.jobs.find().sort("job_name", 1))
        return render_template('profile.html', username=username, jobs=jobs)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash('You have logged out', 'logout-flash')
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        management_is_urgent = "on" if request.form.get("management_is_urgent") else "off"
        employee = {
            "management_employee": request.form.get("management_employee"),
            "management_department": request.form.get("management_department"),
            "management_is_urgent": management_is_urgent,
            "management_start_day": request.form.get("management_start_day"),
            "management_phone": request.form.get("management_phone"),
            "management_email": request.form.get("management_email"),
            "management_manager": session["user"],
            "management_media": request.form.get("management_media")
        }
        mongo.db.employees.insert_one(employee)

        return redirect(url_for("get_employees"))

    management = mongo.db.management.find().sort("management_department", 1)
    return render_template('add_employee.html', management=management)


@app.route('/edit_employee/<employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):

    if request.method == "POST":
        management_is_urgent = "on" if request.form.get("management_is_urgent") else "off"
        employee_edit = {
            "management_employee": request.form.get("management_employee"),
            "management_department": request.form.get("management_department"),
            "management_is_urgent": management_is_urgent,
            "management_start_day": request.form.get("management_start_day"),
            "management_phone": request.form.get("management_phone"),
            "management_email": request.form.get("management_email"),
            "management_manager": session["user"],
            "management_media": session["management_media"]
        }
        mongo.db.employees.update({"_id": ObjectId(employee_id)}, employee_edit)
        return redirect(url_for("get_employees"))
    
    employee = mongo.db.employees.find_one({"_id": ObjectId(employee_id)})
    management = mongo.db.management.find().sort("management_department", 1)
    return render_template('edit_employee.html', employee=employee, management=management)


@app.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):
    mongo.db.employees.remove({"_id": ObjectId(employee_id)})

    return redirect(url_for("get_employees"))


@app.route("/get_departments")
def get_departments():
    departments = list(mongo.db.management.find().sort("management_department", 1))
    return render_template("departments.html", departments=departments)


@app.route("/jobs")
def jobs():
    jobs = list(mongo.db.jobs.find().sort("job_name", 1))
    return render_template("jobs.html", jobs=jobs)


@app.route("/job/<job_id>")
def job(job_id):
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    return render_template("job.html", job=job)


@app.route("/add_departments", methods=["GET", "POST"])
def add_departments():
    if request.method == 'POST':
        management = {
            "management_department": request.form.get("management_department")
        }
        mongo.db.management.insert_one(management)
        return redirect(url_for("get_employees"))

    return render_template("add_departments.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    query = request.form.get("query").lower()
    employees = list(mongo.db.employees.find({"$text": {"$search": query}}))
    return render_template("employees.html", employees=employees)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get('DBUG'))
            
            
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
@app.route("/home")
def home():
    """
    This Function gets the user to the main page.
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "home.html", user=user)
    else:
        return render_template("home.html")


@app.route("/employees")
def employees():
    """
    This function gets all the employees added to the website
    shown on this page.
    """
    employees = list(mongo.db.employees.find())
    return render_template("employees.html", employees=employees)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    This function gets the user redirected to the profile page.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session['user']:
        jobs = list(mongo.db.jobs.find().sort("job_name", 1))
        return render_template('profile.html', username=username, jobs=jobs)

    return redirect(url_for('login'))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This function allows the user to register themselves into
    the website.
    """
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
    """
    This function checks if the user is logging themselves
    using their right info. If they log themslves they get
    redirected to the profile page if not it gives the user
    a red flash.
    """
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


@app.route('/logout')
def logout():
    """
    This function gets the user to be logged out of the website.
    """
    flash('You have logged out', 'logout-flash')
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add", methods=["GET", "POST"])
def add_employee():
    """
    This function gets the user to add employee to the website.
    """
    if request.method == "POST":
        
        management_active = "on" if request.form.get("management_active") else "off"
        employee = {
            "management_employee": request.form.get("management_employee"),
            "management_department": request.form.get("management_department"),
            "management_active": management_active,
            "management_start_day": request.form.get("management_start_day"),
            "management_phone": request.form.get("management_phone"),
            "management_email": request.form.get("management_email"),
            "management_manager": session["user"],
            "management_media": request.form.get("management_media")
        }
        mongo.db.employees.insert_one(employee)

        return redirect(url_for("employees"))

    management = mongo.db.management.find().sort("management_department", 1)
    return render_template('add.html', management=management)


@app.route('/edit/<employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    """
    This function allows the user to edit their existing employees.
    It can only be done if the user was the manager who added
    the employee.
    """
    if request.method == "POST":
        management_active = "on" if request.form.get("management_active") else "off"
        employee_edit = {
            "management_employee": request.form.get("management_employee"),
            "management_department": request.form.get("management_department"),
            "management_active": management_active,
            "management_start_day": request.form.get("management_start_day"),
            "management_phone": request.form.get("management_phone"),
            "management_email": request.form.get("management_email"),
            "management_manager": session["user"],
            "management_media": session["management_media"]
        }
        mongo.db.employees.update({"_id": ObjectId(employee_id)}, employee_edit)
        return redirect(url_for("employees"))
    
    employee = mongo.db.employees.find_one({"_id": ObjectId(employee_id)})
    management = mongo.db.management.find().sort("management_department", 1)
    return render_template('edit.html', employee=employee, management=management)


@app.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):
    """
    This allows the manager to delete a employee who has been 
    added by them.
    """
    mongo.db.employees.remove({"_id": ObjectId(employee_id)})

    return redirect(url_for("employees"))


@app.route("/get_departments")
def get_departments():
    """
    This function is to show user the departments that exist
    within the website.
    """
    departments = list(mongo.db.management.find().sort("management_department", 1))
    return render_template("departments.html", departments=departments)


@app.route("/add_departments", methods=["GET", "POST"])
def add_departments():
    """
    This function allows the Admin of the website to add 
    departments into the website system.
    """
    if request.method == 'POST':
        management = {
            "management_department": request.form.get("management_department")
        }
        mongo.db.management.insert_one(management)
        return redirect(url_for("get_departments"))

    return render_template("add_departments.html")


@app.route("/edit_departments/<department_id>", methods=["GET", "POST"])
def edit_departments(department_id):
    """
    This function allows the admin to edit a department.
    """
    if request.method == "POST":
        submit = {
            "management_department": request.form.get("management_department")
        }
        mongo.db.management.update({"_id": ObjectId(department_id)}, submit)
        return redirect(url_for("get_departments"))
    department = mongo.db.management.find_one({"_id": ObjectId(department_id)})
    return render_template("edit_department.html", department=department)


@app.route("/delete_department/<department_id>")
def delete_department(department_id):
    """
    This function allows the admin to delete a department.
    """
    mongo.db.management.remove({"_id": ObjectId(department_id)})
    flash("Department removed", "danger")
    return redirect(url_for("get_departments"))


@app.route("/jobs")
def jobs():
    """
    This function allows the user to look a few job markets.
    """
    jobs = list(mongo.db.jobs.find().sort("job_name", 1))
    return render_template("jobs.html", jobs=jobs)


@app.route("/job/<job_id>")
def job(job_id):
    """
    This function allows the user to look a specific job market.
    """
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    return render_template("job.html", job=job)



@app.route("/search", methods=["POST", "GET"])
def search():
    """
    This function allows the user to look for an employee
    by their name or by their deparment.
    """
    query = request.form.get("query").lower()
    employees = list(mongo.db.employees.find({"$text": {"$search": query}}))
    return render_template("employees.html", employees=employees)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get('DBUG'))
            
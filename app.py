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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1


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
        return render_template('profile.html', username=username)

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
            "management_media": session["management_media"]
            
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
    flash('You have deleted {{ username }}', 'logout-flash')


@app.route("/get_departments")
def get_departments():
    departments = list(mongo.db.management.find().sort("management_department", 1))
    return render_template("departments.html", departments=departments)


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('profile.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
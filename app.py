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
    return render_template("pages/home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This function allows the user to register themselves into the website system
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for("register"))

        username = request.form.get("username").lower()
        passowrd = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one({
            "username": username,
            "password": passowrd
        })

        if mongo.db.users.find_one({"username": username}) is not None:
            user = mongo.db.users.find_one({"username": username})
            user_id = user["_id"]
            session["user_id"] = str(user_id)
            employees = mongo.db.employees.find({"user_id": user_id})
            return redirect(url_for("empty_dashboard", user_id=user_id))
    
    return render_template("pages/auth.html", register=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function allows the user the log themselves into the website
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"],
            request.form.get("password")):
                user_id = str(existing_user["_id"])
                session["user_id"] = str(user_id)

                employee_profile = mongo.db.employees.find_one({"user_id": user_id})

                if employee_profile:
                    employee_id = employee_profile["_id"]
                    employees = mongo.db.employees.find({"user_id": user_id})
                    return redirect(url_for("view_dashboard", user_id=user_id, employee_id=employee_id))

                else:
                    employees = mongo.db.employees.find({"user_id":user_id})
                    return redirect(url_for("blank_dasboard", user_id=user_id))
        
            else:
                flash("Incorrect Username and/or Password", "danger")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password", "danger")
            return redirect(url_for("login"))

    return render_template("pages/auth.html")




@app.route("/logout")
def logout():
    """
    This function allows user to log themselve out of the website
    """
    flash('You have logged out', 'logout-flash')
    session.clear()
    return render_template("pages/home.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get('DBUG'))
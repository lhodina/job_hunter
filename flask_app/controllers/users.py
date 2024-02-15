from flask import redirect, request, session
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models import user

bcrypt = Bcrypt(app)

@app.route("/login")
def login_and_registration():
    if (session and session["authorization_message"]):
        return {
            "authorization_message": session["authorization_message"]
        }
    else:
        print("loggin in")
        return {
            "message": "loggin' on in, friend!"
        }


@app.route("/register", methods=["POST"])
def register_user():
    print(request.json)
    data = {
        "first_name": request.json["firstName"],
        "last_name": request.json["lastName"],
        "email": request.json["email"],
        "password": request.json["password"],
        "confirm_password": request.json["confirmPassword"]
    }

    validation_messages = user.User.validate_user(data)
    if len(validation_messages) > 0:
        return {"validation_messages": validation_messages}
    else:
        session.clear()
        pw_hash = bcrypt.generate_password_hash(request.json['password'])
        print("pw_hash:", pw_hash)
        data["password"] = pw_hash
        user_id = user.User.save(data)
        current_user = user.User.get_one({"id": user_id})

        session["user"] = {
            "id": current_user.id,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name
        }

        session.modified = True
        return {"testing response": "testtest"}


@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.json["email"],
        "password": request.json["password"]
    }

    session["login_data"] = data
    validation_messages = user.User.validate_login(data)
    if len(validation_messages) < 1:
        session.clear()
        current_user = user.User.get_by_email({"email": data["email"]})[0]
        session["user"] = {
            "id": current_user['id'],
            "first_name": current_user['first_name'],
            "last_name": current_user['last_name']
        }
        return redirect("/dashboard")
    else:
        return {"validation_messages": validation_messages}



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re


bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = re.compile(r"^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\-\#\$\.\%\&\*\@\!]{8,}$")

class User:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s )
        """
        return connectToMySQL(cls.DB).query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        current_user_data = {
            "id": result[0]["id"],
            "first_name": result[0]["first_name"],
            "last_name": result[0]["last_name"],
            "email": result[0]["email"],
            "password": result[0]["password"],
            "created_at": result[0]["created_at"],
            "updated_at": result[0]["updated_at"],
        }

        current_user = cls(current_user_data)
        return current_user


    @classmethod
    def get_by_email(cls, user_email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        return connectToMySQL(cls.DB).query_db(query, user_email)


    @staticmethod
    def validate_user(user):
        messages = []
        if not user["first_name"]:
            messages.append("First name required")
        elif len(user["first_name"]) < 2:
            messages.append("First name must be at least two characters")
        if not user["last_name"]:
            messages.append("Last name required")
        elif len(user["last_name"]) < 2:
            messages.append("Last name must be at least two characters")
        if not user["email"]:
            messages.append("Email required")
        elif not EMAIL_REGEX.match(user["email"]):
            messages.append("Email must be in the following format: beeblebrox@galaxy.gov")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email": user["email"]}
        res = connectToMySQL("job_hunter").query_db(query, data)
        if res:
            messages.append("Email already in use")
        if not user["password"]:
            messages.append("Password required")
        elif user["password"] != user["confirm_password"]:
            messages.append("Passwords do not match")
        elif not PASSWORD_REGEX.match(user["password"]):
            messages.append("Password must include 1 capital letter and 1 number")
        return messages


    @staticmethod
    def validate_login(data):
        messages = []
        if not data["email"]:
            messages.append("Email Required")
        elif not EMAIL_REGEX.match(data["email"]):
            messages.append("Email must be in the following format: beeblebrox@galaxy.gov")
        else:
            query = "SELECT * FROM users WHERE email = %(email)s;"
            result = connectToMySQL("job_hunter").query_db(query, {"email": data["email"]})
            current_user = None
            if not result:
                messages.append("Email not found")
            else:
                current_user = result[0]
            if current_user and not bcrypt.check_password_hash(current_user["password"], data["password"]):
                messages.append("Incorrect password")
        if not data["password"]:
            messages.append("Password required")
        return messages


    @classmethod
    def get_all_user_content(cls, data):
        query = """
            SELECT * FROM tags
            LEFT JOIN notes ON notes.user_id = %(user_id)s
            WHERE tags.user_id = %(user_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

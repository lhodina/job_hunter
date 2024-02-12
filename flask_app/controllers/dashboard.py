from flask import redirect, request, session
from flask_app import app
from flask_app.models import category, tag

@app.route("/dashboard")
def dashboard():
    if not (session and session["user"]):
        session["authorization_message"] = "You must be logged in to view the dashboard"
        return redirect("/login")
    else:
        data = {
            "user_id": session["user"]["id"]
        }
        print("data: ", data)
        all_categories = category.Category.get_all_categories()
        all_tags = tag.Tag.get_all_tags(data)
        # user_links = link.Link.get_user_links(data)
        print("***** all_categories: ", all_categories)
        print()
        print("***** all_tags: ", all_tags)
        print()
        # print("***** all_user_links: ", all_user_links)
        return {
            "user_id": session["user"]["id"],
            "user_first_name": session["user"]["first_name"],
            "user_last_name": session["user"]["last_name"]
        }

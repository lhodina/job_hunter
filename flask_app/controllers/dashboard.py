from flask import redirect, request, session
from flask_app import app
from flask_app.models import user, category, tag, link

@app.route("/dashboard")
def dashboard():
    if not (session and session["user"]):
        session["authorization_message"] = "You must be logged in to view the dashboard"
        return redirect("/login")
    else:
        data = {
            "user_id": session["user"]["id"]
        }

        categories = [
            {"id": 1, "name": "Interests"},
            {"id": 2, "name": "Contacts"},
            {"id": 3, "name": "Companies"},
            {"id": 4, "name": "Locations"},
        ]

        all_tags = []
        links = []
        tag_names = []
        link_text = []

        all_user_content = user.User.get_all_user_content(data)
        for item in all_user_content:
            print(item)
            print("")
            if (item["text"] not in tag_names):
                tag_names.append(item["text"])
                all_tags.append({
                    "id": item["id"],
                    "text": item["text"],
                    "user_id": item["user_id"],
                    "category_id": item["category_id"]
                })
            if (item["links.text"] not in link_text):
                link_text.append(item["links.text"])
                links.append({
                    "id": item["links.id"],
                    "text": item["links.text"],
                    "url": item["url"],
                    "category_id": item["links.category_id"],
                    "user_id": item["links.user_id"]
                })
        interests = list(filter(lambda d: d["category_id"] == 1, all_tags))
        contacts = list(filter(lambda d: d["category_id"] == 2, links))
        companies = list(filter(lambda d: d["category_id"] == 3, all_tags))
        locations = list(filter(lambda d: d["category_id"] == 4, all_tags))
        return {
            "user_id": session["user"]["id"],
            "user_first_name": session["user"]["first_name"],
            "user_last_name": session["user"]["last_name"],
            "categories": categories,
            "all_tags": all_tags,
            "links": links,
            "interests": interests,
            "contacts": contacts,
            "companies": companies,
            "locations": locations
        }

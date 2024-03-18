from flask import redirect, request, session
from flask_app import app
from flask_app.models import note, user, category, tag

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
        notes = []
        tag_names = []
        note_ids = []

        all_user_content = user.User.get_all_user_content(data)
        for item in all_user_content:
            # print(item)
            # print("")
            if (item["text"] not in tag_names):
                tag_names.append(item["text"])
                all_tags.append({
                    "id": item["id"],
                    "text": item["text"],
                    "user_id": item["user_id"],
                    "category_id": item["category_id"]
                })
            if (item["notes.id"] not in note_ids):
                note_ids.append(item["notes.id"])
                notes.append({
                    "id": item["notes.id"],
                    "text": item["notes.text"],
                    "link_text": item["link_text"],
                    "link_url": item["link_url"],
                    "category_id": item["notes.category_id"],
                    "user_id": item["notes.user_id"]
                })
        interests = list(filter(lambda d: d["category_id"] == 1, all_tags))
        contacts = list(filter(lambda d: d["category_id"] == 2, notes))
        companies = list(filter(lambda d: d["category_id"] == 3, all_tags))
        locations = list(filter(lambda d: d["category_id"] == 4, all_tags))
        return {
            "user_id": session["user"]["id"],
            "user_first_name": session["user"]["first_name"],
            "user_last_name": session["user"]["last_name"],
            "categories": categories,
            "all_tags": all_tags,
            "notes": notes,
            "interests": interests,
            "contacts": contacts,
            "companies": companies,
            "locations": locations
        }

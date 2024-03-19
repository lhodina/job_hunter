from flask import request, session

from flask_app import app
from flask_app.models import note, tag

@app.route("/contacts/<int:id>")
def get_contact(id):
    user_id = session["user"]["id"]
    data = {"id": id }
    tag_ids = []
    tags = []
    res = note.Note.get_contact(data)
    for item in res:
        if (item["tag_id"] and item["tag_id"] not in tag_ids):
            tag_ids.append(item["tag_id"])
            current_tag = {
                "id": item["tag_id"],
                "text": item["tags.text"],
                "category_id": item["tags.category_id"]
            }
            tags.append(current_tag)
        # print(item)
        # print("")

    interests = list(filter(lambda d: d["category_id"] == 1, tags))
    companies = list(filter(lambda d: d["category_id"] == 3, tags))
    locations = list(filter(lambda d: d["category_id"] == 4, tags))
    return {
        "user_id": user_id,
        "name": res[0]["link_text"],
        "description": res[0]["text"],
        "linked_in_url": res[0]["link_url"],
        "interests": interests,
        "companies": companies,
        "locations": locations
    }

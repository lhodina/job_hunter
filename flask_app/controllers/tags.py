from flask import redirect, request, session

from flask_app import app
from flask_app.models import tag

@app.route("/tags/<int:tag_id>")
def get_tag(tag_id):
    user_id = session["user"]["id"]
    data = {
        "user_id": user_id,
        "tag_id": tag_id
    }
    current_tag = tag.Tag.get_one(data)

    related_tags = []
    related_tag_ids = []
    notes = []
    note_ids = []

    for item in current_tag:
        if (item["related_tags.id"] and item["related_tags.id"] not in related_tag_ids):
            related_tag_ids.append(item["related_tags.id"])
            relatedTag = {}
            relatedTag["id"] = item["related_tags.id"]
            relatedTag["text"] = item["related_tags.text"]
            relatedTag["user_id"] = item["user_id"]
            relatedTag["category_id"] = item["related_tags.category_id"]
            related_tags.append(relatedTag)
        if (item["notes.id"] and item["notes.id"] not in note_ids):
            note_ids.append(item["notes.id"])
            currentNote = {}
            currentNote["id"] = item["notes.id"]
            currentNote["text"] = item["notes.text"]
            currentNote["link_text"] = item["link_text"]
            currentNote["link_url"] = item["link_url"]
            currentNote["category_id"] = item["notes.category_id"]
            currentNote["user_id"] = item["notes.user_id"]
            notes.append(currentNote)

    contacts = list(filter(lambda d: d["category_id"] == 2, notes))
    user_notes = list(filter(lambda d: d["category_id"] != 2, notes))
    interests = list(filter(lambda d: d["category_id"] == 1, related_tags))
    companies = list(filter(lambda d: d["category_id"] == 3, related_tags))

    return {
        "user_id": user_id,
        "first_name": session["user"]["first_name"],
        "last_name": session["user"]["last_name"],
        "text": current_tag[0]["text"],
        "interests": interests,
        "companies": companies,
        "contacts": contacts,
        "notes": user_notes
    }

@app.route("/tags/<string:tagType>", methods=["POST"])
def add_tag(tagType):
    category_id = None
    if (tagType == "Interest"):
        category_id = 1
    elif (tagType == "Company"):
        category_id = 3
    elif (tagType == "Location"):
        category_id = 4
    print("category_id: ", category_id)
    data = {
        "text": request.json["text"],
        "category_id": category_id,
        "user_id": session["user"]["id"]
    }
    res = tag.Tag.save(data)
    print("res: ", res)
    return {"id": res}

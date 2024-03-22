from flask import redirect, request, session

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

@app.route("/contacts", methods=["POST"])
def add_contact():
    print("CONTROLLER - request.json: ", request.json)
    data = {
        "user_id": session["user"]["id"],
        "text": request.json["description"],
        "link_text": request.json["name"],
        "link_url": request.json["linkedInUrl"],
        "category_id": 2
    }
    print("CONTROLLER data: ", data)
    note_id = note.Note.save(data)
    print("CONTROLLER note_id: ", note_id)
    if (request.json["currentPageId"]):
        tag.Tag.join_to_note({"tag_id": request.json["currentPageId"], "note_id": note_id})
    return {"id": note_id}


@app.route("/contacts/<int:contactId>/update", methods=["POST"])
def update_contact(contactId):
    print("CONTROLLER - request.json: ", request.json)
    data = {
        "user_id": session["user"]["id"],
        "contact_id": contactId,
        "link_text": request.json["name"],
        "link_url": request.json["linkedInUrl"],
        "category_id": 2
    }
    note_id = note.Note.update_contact(data)
    return {"id": note_id}


@app.route("/contacts/<int:id>/delete", methods=["POST"])
def delete_contact(id):
    data = {
        "id": id
    }
    note.Note.delete(data)
    return redirect("/dashboard")

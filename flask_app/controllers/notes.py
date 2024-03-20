from flask import request, session

from flask_app import app
from flask_app.models import note, tag

@app.route("/notes", methods=["POST"])
def add_note():
    print("CONTROLLER - request.json: ", request.json)

    data = {
        "user_id": session["user"]["id"],
        "text": request.json["text"],
        "link_text": request.json["linkText"],
        "link_url": request.json["linkUrl"],
        "category_id": None
    }
    print("CONTROLLER data: ", data)
    note_id = note.Note.save(data)
    print("CONTROLLER note_id: ", note_id)
    tag.Tag.join_to_note({"tag_id": request.json["currentPageId"], "note_id": note_id})
    return {"id": note_id}

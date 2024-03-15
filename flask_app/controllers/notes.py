from flask import redirect, request, session

from flask_app import app
from flask_app.models import note, tag

@app.route("/notes/<string:noteType>", methods=["POST"])
def add_note(noteType):
    print("CONTROLLER - request.json: ", request.json)
    category_id = None
    if (noteType == "Contact"):
        category_id = 2

    print("CONTROLLER category_id: ", category_id)

    data = {
        "user_id": session["user"]["id"],
        "text": request.json["text"],
        "category_id": category_id,
        "link_text": request.json["linkText"],
        "link_url": request.json["linkUrl"]
    }
    print("CONTROLLER data: ", data)
    new_note_id = note.Note.save(data)
    print("CONTROLLER new_note_id: ", new_note_id)

    if (request.json["currentPageId"]):
        # Join tag with tag
        tag.Tag.join_to_note({"tag_id": request.json["currentPageId"], "note_id": new_note_id})

    return {"id": new_note_id}

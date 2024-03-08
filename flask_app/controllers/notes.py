from flask import redirect, request, session

from flask_app import app
from flask_app.models import note

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
    res = note.Note.save(data)
    print("CONTROLLER res: ", res)
    return {"id": res}

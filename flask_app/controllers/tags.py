from flask import redirect, request, session

from flask_app import app
from flask_app.models import user, tag

@app.route("/tags/<int:tag_id>")
def get_tag(tag_id):
    user_id = session["user"]["id"]
    data = {
        "id": tag_id
    }

    current_tag = tag.Tag.get_one(data)

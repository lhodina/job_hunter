from flask import redirect, request, session

from flask_app import app
from flask_app.models import user, tag, link

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
    all_links = []
    all_link_ids = []
    notes = []
    notes_ids = []

    for item in current_tag:
        print("")
        print(item)
        print("")
        if (item["related_tags.id"] and item["related_tags.id"] not in related_tag_ids):
            related_tag_ids.append(item["related_tags.id"])
            relatedTag = {}
            relatedTag["id"] = item["related_tags.id"]
            relatedTag["text"] = item["related_tags.text"]
            relatedTag["user_id"] = item["user_id"]
            relatedTag["category_id"] = item["related_tags.category_id"]
            related_tags.append(relatedTag)
        if (item["links.id"] and item["links.id"] not in all_link_ids):
            all_link_ids.append(item["links.id"])
            currentLink = {}
            currentLink["id"] = item["links.id"]
            currentLink["text"] = item["links.text"]
            currentLink["url"] = item["url"]
            currentLink["category_id"] = item["links.category_id"]
            currentLink["user_id"] = item["links.user_id"]
            all_links.append(currentLink)
        if (item["notes.id"] and item["notes.id"] not in notes_ids):
            notes_ids.append(item["notes.id"])
            currentNote = {}
            currentNote["id"] = item["notes.id"]
            currentNote["text"] = item["notes.text"]
            currentNote["user_id"] = item["notes.user_id"]
            notes.append(currentNote)

    print("all_links: ", all_links)
    # print("related_tags: ", related_tags)
    contacts = list(filter(lambda d: d["category_id"] == 2, all_links))
    user_links = list(filter(lambda d: d["category_id"] != 2, all_links))
    interests = list(filter(lambda d: d["category_id"] == 1, related_tags))
    companies = list(filter(lambda d: d["category_id"] == 3, related_tags))

    return {
        "user_id": user_id,
        "first_name": session["user"]["first_name"],
        "last_name": session["user"]["last_name"],
        "text": current_tag[0]["text"],
        "interests": interests,
        "companies": companies,
        "user_links": user_links,
        "contacts": contacts,
        "notes": notes
    }

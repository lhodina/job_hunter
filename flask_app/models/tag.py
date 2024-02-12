from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import link

class Tag:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.user_id = data['user_id']
        self.links = []

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO tags(text, category_id, user_id)
        VALUES ( %(name)s, %(category_id)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_tags(cls, data):
        all_tags = []
        query = """
        SELECT * FROM tags
        WHERE user_id = %(user_id)s OR user_id = 1;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_tags.append(result)
        return all_tags

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM tags
        WHERE tags.id = %(tag_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)[0]

    @classmethod
    def get_tag_links(cls, data):
        tag_links = []
        query = """
        SELECT * FROM links
        JOIN links_join_tags ON links_join_tags.link_id = links.id
        JOIN tags ON tags.id = link_join_tags.tag_id
        WHERE tags.id = %(tag_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            current_link_data = {
                "id": result["id"],
                "text": result["text"],
                "url": result["url"],
                "created_at": result["created_at"],
                "updated_at": result["updated_at"],
                "user_id": result["user_id"],
                "category_id": result["category_id"]
            }
            current_link = link.Link(current_link_data)
            tag_links.append(current_link)
        return tag_links

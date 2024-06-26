from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import note

class Tag:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO tags(text, category_id, user_id)
        VALUES ( %(text)s, %(category_id)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_tags_in_category(cls, data):
        all_tags = []
        query = """
        SELECT * FROM tags
        WHERE user_id = %(user_id)s AND category_id = %(category_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_tags.append(result)
        return all_tags

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM tags
        LEFT JOIN tags_join_tags ON tags_join_tags.tag_id_1 = tags.id
        LEFT JOIN tags AS related_tags ON related_tags.id = tags_join_tags.tag_id_2
        LEFT JOIN tags_join_notes ON tags_join_notes.tag_id = %(tag_id)s
        LEFT JOIN notes ON notes.id = tags_join_notes.note_id
        WHERE tags.id = %(tag_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_name(cls, data):
        query = """
        SELECT * FROM tags
        WHERE text = %(text)s AND user_id = %(user_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def join_to_tag(cls, data):
        query = """
        INSERT INTO tags_join_tags(tag_id_1, tag_id_2)
        VALUES (%(tag_id_1)s, %(tag_id_2)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def join_to_note(cls, data):
        query = """
        INSERT INTO tags_join_notes(tag_id, note_id)
        VALUES (%(tag_id)s, %(note_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE tags
        SET text = %(text)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM tags
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

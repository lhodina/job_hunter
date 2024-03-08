from flask_app.config.mysqlconnection import connectToMySQL

class Note:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.link_text = data['link_text']
        self.link_url = data['link_url']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO notes(text, link_text, link_url, user_id, category_id)
        VALUES ( %(text)s, %(link_text)s, %(link_url)s, %(user_id)s, %(category_id)s );
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_user_notes(cls, data):
        all_notes = []
        query = """
        SELECT * FROM notes
        WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_notes.append(result)
        return all_notes

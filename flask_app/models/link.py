from flask_app.config.mysqlconnection import connectToMySQL

class Link:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.url = data['url']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.category_id = data['category_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO links(text, url, user_id, category_id)
        VALUES ( %(text)s, %(url)s, %(user_id)s, %(category_id)s, )
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_user_links(cls, data):
        all_links = []
        query = """
        SELECT * FROM links
        WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_links.append(result)
        return all_links

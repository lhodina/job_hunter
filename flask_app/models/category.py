from flask_app.config.mysqlconnection import connectToMySQL

class Category:
    DB = "job_hunter"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_categories(cls):
        all_categories = []
        query = """
        SELECT * FROM categories;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        for result in results:
            all_categories.append(result)
        return all_categories

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM categories
        WHERE categories.id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

from flask_mysqldb import MySQL


class DatabaseManager:
    def __init__(self, app):
        self.name = None
        self.email = None
        self.app = app

        self.app.config['MYSQL_USER'] = 'sql11411272'
        self.app.config['MYSQL_PASSWORD'] = '4PMPh7NtCA'
        self.app.config['MYSQL_HOST'] = 'sql11.freemysqlhosting.net'
        self.app.config['MYSQL_DB'] = 'sql11411272'
        self.app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

        self.mysql = MySQL(self.app)
        self.cursor = None

    def create_table(self):
        self.cursor = self.mysql.connection.cursor()
        try:
            self.cursor.execute('CREATE TABLE users (name TEXT, email TEXT)')
        except:
            pass

    def add_user(self, name, email):
        self.cursor = self.mysql.connection.cursor()
        self.cursor.execute(f"INSERT INTO users VALUES('{name}', '{email}')")
        self.mysql.connection.commit()

    def get_users(self):
        self.cursor = self.mysql.connection.cursor()
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
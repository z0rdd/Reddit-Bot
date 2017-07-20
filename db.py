import psycopg2
import urllib.parse as urlparse
import os
from datetime import datetime


class Database:

    def __init__(self, heroku):

        if heroku:
            self.url_heroku = urlparse.urlparse(os.environ['DATABASE_URL'])
            self.dbname = self.url_heroku.path[1:]
            self.user = self.url_heroku.username
            self.password = self.url_heroku.password
            self.host = self.url_heroku.hostname
            self.port = self.url_heroku.port
        else:
            self.dbname = "flaskapp"
            self.user = "postgres"
            self.password = "aaa"
            self.host = "localhost"
            self.port = "5432"

        self.create_table()

    def create_table(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stats (id serial PRIMARY KEY, comment_id VARCHAR,"
                    " author VARCHAR, hit_count INTEGER, date TIMESTAMPTZ)")
        conn.commit()
        conn.close()

    def insert(self, comment_id, author, hit_count):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        cur = conn.cursor()
        cur.execute("INSERT INTO stats (comment_id, author, hit_count, date) VALUES (%s, %s, %s, %s)",
                    (comment_id, author, hit_count, datetime.now()))
        conn.commit()
        conn.close()

    def search_comment_id(self, comment_id):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        cur = conn.cursor()
        cur.execute("SELECT * FROM stats WHERE comment_id = %s", (comment_id,))
        row = cur.fetchone()
        conn.close()
        return row

    def view_all(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        cur = conn.cursor()
        cur.execute("SELECT * FROM stats")
        rows = cur.fetchall()
        conn.close()
        return rows

if __name__ == "__main__":
    db = Database()
    print(db.search_comment_id("sfds"))



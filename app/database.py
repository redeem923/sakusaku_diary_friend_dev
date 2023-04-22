import sqlite3


class Database:

    def __init__(self, db_name="chatbot.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                state TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diaries (
                id INTEGER PRIMARY KEY,
                user_id TEXT NOT NULL,
                entry TEXT NOT NULL,
                topic_vector TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def get_user_state(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT state FROM users WHERE id=?", (user_id,))

        result = cursor.fetchone()
        return result[0] if result else None

    def set_user_state(self, user_id, new_state):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO users (id, state)
            VALUES (?, ?)
        """, (user_id, new_state))

        self.conn.commit()
        return True

    def save_diary_entry(self, user_id, diary_entry, topic_vector):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO diaries (user_id, entry, topic_vector)
            VALUES (?, ?, ?)
        """, (user_id, diary_entry, topic_vector))

        self.conn.commit()
        return True

    def get_past_diary_data(self, user_id, topic_vector):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT entry
            FROM diaries
            WHERE user_id=? AND topic_vector=?
        """, (user_id, topic_vector))

        result = cursor.fetchall()
        return [row[0] for row in result] if result else None

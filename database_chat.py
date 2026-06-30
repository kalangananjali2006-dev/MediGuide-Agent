import sqlite3


DB_NAME = "mediguide.db"



def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chats
        (
            username TEXT,
            agent TEXT,
            question TEXT,
            response TEXT
        )
        """
    )


    conn.commit()

    conn.close()



def save_chat(username, agent, question, response):

    create_table()


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO chats
        (
            username,
            agent,
            question,
            response
        )

        VALUES (?, ?, ?, ?)
        """,

        (
            username,
            agent,
            question,
            response
        )
    )


    conn.commit()

    conn.close()



def get_chats(username):

    create_table()


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT agent, question, response
        FROM chats
        WHERE username=?
        """,

        (
            username,
        )
    )


    chats = cursor.fetchall()


    conn.close()


    return chats

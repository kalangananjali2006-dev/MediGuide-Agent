import sqlite3


def save_chat(username, agent, question, response):

    conn = sqlite3.connect(
        "mediguide.db"
    )

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


    cursor.execute(
        """
        INSERT INTO chats
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

    conn = sqlite3.connect(
        "mediguide.db"
    )

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT agent, question, response
        FROM chats
        WHERE username=?
        """,
        (username,)
    )


    data = cursor.fetchall()

    conn.close()

    return data

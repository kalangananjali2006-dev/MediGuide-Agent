import sqlite3
import hashlib


def create_database():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT
        )
        """
    )

    conn.commit()
    conn.close()



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def create_user(username, password):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO users VALUES (?,?)",
            (
                username,
                hash_password(password)
            )
        )

        conn.commit()

        result = True

    except:

        result = False


    conn.close()

    return result



def check_user(username, password):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (
            username,
            hash_password(password)
        )
    )


    result = cursor.fetchone()

    conn.close()


    return result is not None

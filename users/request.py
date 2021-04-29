import sqlite3
import json


def register_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # insert new user info into database
        db_cursor.execute("""
        INSERT INTO Users
            ( first_name, last_name, display_name, email, password )
        VALUES
            ( ?, ?, ?, ?, ? );
        """, (new_user['first_name'],
              new_user['last_name'],
              new_user['username'],
              new_user['email'],
              new_user['password']))

        # create id for new user
        id = db_cursor.lastrowid
        new_user['id'] = id

        response_object = {
            "valid": True,
            "token": new_user['id']
        }

    return json.dumps(response_object)

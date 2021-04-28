import sqlite3
import json
from models import User


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


def get_users_by_login(email, password):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.email,
            u.password
        from Users u
        WHERE u.email = ? 
        AND u.password = ?
        """, (email, password))

        data = db_cursor.fetchone()

        if data['id']:
            user_auth = {'valid': True, 'token': data['id']}
            return json.dumps(user_auth)

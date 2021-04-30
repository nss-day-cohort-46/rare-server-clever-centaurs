import sqlite3
import json
from models import Tag


def get_all_tags():

    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label 
        FROM Tags t
        ORDER BY t.label COLLATE NOCASE ASC
        """ )

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

        return json.dumps(tags)

def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            (label)
            VALUES (?);   
        """, 
        (new_tag['label'], ))

        id = db_cursor.lastrowid

        new_tag['id'] = id
    
    return json.dumps(new_tag)

def update_tag(id, new_tag):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE categories
            SET
                label = ?
        WHERE id = ?
        """, (new_tag['label'],id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tags
        WHERE id = ?
        """, (id, ))

def get_single_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        WHERE t.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        tag = Tag(data['id'], data['label'])

        return json.dumps(tag.__dict__)

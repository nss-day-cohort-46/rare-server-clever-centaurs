import sqlite3
import json

from models import Post

def update_post(id, new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Posts
            SET 
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                content = ?
        WHERE id = ?
        """, (new_post['user_id'], 
        new_post['category_id'], 
        new_post['title'], 
        new_post['publication_date'], 
        new_post['content']))

        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
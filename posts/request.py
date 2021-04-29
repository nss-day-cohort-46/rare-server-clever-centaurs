import sqlite3
import json
from models import Post

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.content
            FROM Posts p
        """)

        # Initialize an empty list to hold all post representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                            row['publication_date'], row['content'])

            # # Create a User instance from the current row
            # user = User(
            #     row['user_id'], row['user_name'])

            # # Create a Category instance from the current row
            # category = Category(
            #     row['category_id'], row['category_name'])

            # # Add the dictionary representation of the user to the post
            # post.user = user.__dict__
            # post.category = category.__dict__

            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_post_by_id(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM Posts p
        WHERE p.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an post instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['content'])

        return json.dumps(post.__dict__)
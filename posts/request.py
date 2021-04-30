import sqlite3
import json
from models import Post, User, Category, category


def get_all_posts():
    with sqlite3.connect("./rare.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.content,
                u.first_name,
                u.last_name,
                u.display_name,
                u.email,
                u.password,
                c.label
            FROM Posts p
            JOIN users u
                ON u.id = p.user_id
            JOIN categories c
                ON c.id = p.category_id
        """
        )

        # Initialize an empty list to hold all post representations
        posts = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an post instance from the current row
            post = Post(
                row["id"],
                row["user_id"],
                row["category_id"],
                row["title"],
                row["publication_date"],
                row["content"],
            )

            user = User(
                row["id"],
                row["first_name"],
                row["last_name"],
                row["display_name"],
                row["email"],
                row["password"],
            )
            # Add the dictionary representation of the post to the list
            category = Category(row["id"], row["label"])

            post.user = user.__dict__
            post.category = category.__dict__
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_post_by_id(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            u.first_name,
            u.last_name,
            u.display_name,
            u.email,
            u.password,
            c.label
        FROM Posts p
        JOIN Users u 
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an post instance from the current row
        post = Post(
            data["id"],
            data["user_id"],
            data["category_id"],
            data["title"],
            data["publication_date"],
            data["content"],
        )

        user = User(
            data["id"],
            data["first_name"],
            data["last_name"],
            data["display_name"],
            data["email"],
            data["password"],
        )

        category = Category( data["id"], data["label"])
        post.user = user.__dict__
        post.category = category.__dict__

    return json.dumps(post.__dict__)


def add_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        INSERT INTO Posts
            ( title, publication_date, content )
        VALUES 
            ( ?, ?, ?);
        """,
            (new_post["title"], new_post["publication_date"], new_post["content"]),
        )
        id = db_cursor.lastrowid
        new_post["id"] = id

    return json.dumps(new_post)


def get_posts_by_user_id(user_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.content,
                u.first_name,
                u.last_name,
                u.display_name,
                u.email,
                u.password,
                c.label
            FROM Posts p
            JOIN categories c
                ON c.id = p.category_id
            
            JOIN users u ON u.id = p.user_id
            WHERE p.user_id = ? 
            """,
            (user_id,),
        )

        # Initialize an empty list to hold all post representations
        posts = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:
            # Create an post instance from the current row
            post = Post(
                row["id"],
                row["user_id"],
                row["category_id"],
                row["title"],
                row["publication_date"],
                row["content"],
            )

            # Create a User instance from the current row
            user = User(
                row["id"],
                row["first_name"],
                row["last_name"],
                row["display_name"],
                row["email"],
                row["password"],
            )

            post.user = user.__dict__

            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def update_post(id, new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        UPDATE Posts
            SET 
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                content = ?
        WHERE id = ?
        """,
            (
                new_post["user_id"],
                new_post["category_id"],
                new_post["title"],
                new_post["publication_date"],
                new_post["content"],
                id,
            ),
        )

        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

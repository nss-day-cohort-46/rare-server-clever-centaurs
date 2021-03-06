from categories.request import delete_category
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from tags import get_all_tags, create_tag, delete_tag, get_single_tag, update_tag
from categories import get_all_categories, get_single_category, create_category, update_category
from posts.request import get_posts_by_user_id
from posts import (get_all_posts, get_post_by_id, update_post, add_post)
from users import register_user, get_users_by_login


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'posts'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'user_id'
            value = pair[1]  # 'jenna@solis.com'

            return (resource, key, value)

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed
            # fixed tag into tags
            if resource == "tags":
                if id is not None:
                    response = f"{get_single_tag(id)}"
                else:
                    response = f"{get_all_tags()}"
            if resource == "posts":
                if id is not None:
                    response = f"{get_post_by_id(id)}"
                else:
                    response = f"{get_all_posts()}"
            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            if resource == "posts":
                if id is not None:
                    response = f"{get_post_by_id(id)}"
                else:
                    response = f"{get_all_posts()}"
        elif len(parsed) == 3:
            (resource, key, value) = parsed
            if resource == "posts":
                response = f"{get_posts_by_user_id(value)}"

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_item = None
        if resource == "register":
            new_item = register_user(post_body)

        if resource == "tags":
            new_item = create_tag(post_body)

        if resource == "login":
            new_item = get_users_by_login(
                post_body['email'], post_body['password'])

        if resource == "categories":
            new_item = create_category(post_body)

        if resource == "posts":
            new_item = add_post(post_body)

        self.wfile.write(new_item.encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        success = False
        if resource == "posts":
            success = update_post(id, post_body)
        if resource == "tags":
            success = update_tag(id, post_body)

            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)
        if resource == "categories":
            success = update_category(id, post_body)
            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single tag from the list
        if resource == "tags":
            delete_tag(id)
        if resource == "categories":
            delete_category(id)

        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()

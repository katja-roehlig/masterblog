from flask import Flask, render_template
import json

app = Flask(__name__)
# posts = [
#     {
#         "id": 1,
#         "author": "John Doe",
#         "title": "First Post",
#         "content": "This is my first post.",
#     },
#     {
#         "id": 2,
#         "author": "Jane Doe",
#         "title": "Second Post",
#         "content": "This is another post.",
#     },
# ]
# with open("blog_storage.json", "w") as newfile:
#     json_string = json.dumps(posts)
#     newfile.write(json_string)


@app.route("/")
def hello_world():
    with open("blog_storage.json", "r") as file:
        blog_list = json.loads(file.read())
        print(blog_list)
        return render_template("index.html", blogs=blog_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

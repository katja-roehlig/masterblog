from flask import Flask, redirect, render_template, request, url_for
import json
import uuid
import random

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
def index():
    with open("blog_storage.json", "r") as file:
        blog_list = json.load(file)
        return render_template("index.html", blogs=blog_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_id = random.randint(1, 1000000)
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        new_blog = {"id": new_id, "title": title, "author": author, "content": content}
        with open("blog_storage.json", "r") as file:
            blog_list = json.load(file)
        blog_list.append(new_blog)
        with open("blog_storage.json", "w") as newfile:
            json.dump(blog_list, newfile)
        return redirect(url_for("index"))
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

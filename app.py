from flask import Flask, redirect, render_template, request, url_for
import json
import random

app = Flask(__name__)


def load_posts():
    """
    Get the blog list from the json file
    :return blog list
    """
    with open("blog_storage.json", "r") as file:
        blog_list = json.load(file)
        return blog_list


def save_posts(blog_list):
    """
    Saves the blog list in the json file

    :param blog list
    """
    with open("blog_storage.json", "w") as newfile:
        json.dump(blog_list, newfile)


@app.route("/")
def index():
    """
    Displays all blogs using index.html
    """
    with open("blog_storage.json", "r") as file:
        blog_list = json.load(file)
        return render_template("index.html", blogs=blog_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Adds a new blog entry, saves it, and displays it
    """
    if request.method == "POST":
        new_id = random.randint(1, 1000000)
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        new_blog = {"id": new_id, "title": title, "author": author, "content": content}
        blog_list = load_posts()
        blog_list.append(new_blog)
        save_posts(blog_list)

        return redirect(url_for("index"))
    else:
        return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    """
    Deletes a blog entry from the list

    :param id of the blog entry
    """
    blog_list = load_posts()
    new_list = [post for post in blog_list if post["id"] != post_id]
    save_posts(new_list)
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """
    Updates a blog entry and displays the entire blog list

    :param id of the blog to be edited
    """
    blog_list = load_posts()
    blog_found = False
    for blog in blog_list:
        if blog["id"] == post_id:
            editing_post = blog
            blog_found = True
    if not blog_found:
        return "Post not found", 404

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        new_blog = {"title": title, "author": author, "content": content}
        editing_post.update(new_blog)
        save_posts(blog_list)
        return redirect(url_for("index"))

    return render_template("update.html", blog=editing_post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

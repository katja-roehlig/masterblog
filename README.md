# Flask JSON Blog

A lightweight web application built with **Python** and **Flask** that allows users to manage blog posts. This project implements full **CRUD** (Create, Read, Update, Delete) functionality using a local **JSON file** for persistent data storage.

## Features

- **Read**: Display all blog posts from the JSON storage on the home page.
- **Create**: Add new blog posts with a unique ID via a dedicated form.
- **Update**: Edit existing posts (title, author, content) through a pre-filled form.
- **Delete**: Remove posts securely from the storage using POST requests.
- **Persistent Storage**: Data is saved in a `blog_storage.json` file, ensuring posts remain available after server restarts.

## Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, Jinja2 Templates, CSS3 (Custom Styling)
- **Data**: JSON (File-based storage)

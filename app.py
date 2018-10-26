from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
	return "Hello World"

@flask_app.route("/admin/")
def view_admin():
	return "Hello Admin"

@flask_app.route("/admin/<string:name>")
def view_admin_name(name):
	return "Hello {}".format(name)

@flask_app.route("/article/<int:art_id>")
def view_article(art_id):
	return "Article {}".format(art_id)
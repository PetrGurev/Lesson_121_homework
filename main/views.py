from flask import Blueprint, render_template, request
import functions
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search/")
def search_page():
    s = request.args['s']
    posts = functions.search_posts(s)
    return render_template("post_list.html", posts=posts, s=s)
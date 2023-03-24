import json
import re
from pprint import pprint
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

allowed_extensions = ['png', 'jpeg', 'jpg']
FILE_PATH = "posts.json"

class NotAllowedExtension(Exception):
    pass


def load_data():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        logging.info("Файл не найден")
        return []


# search posts by tag
def search_posts(tag):
    sorted_posts = []
    posts = load_data()
    for post in posts:
        if tag in post["content"]:
            sorted_posts.append(post)

    logging.info(f"Поиск по тегу {tag}")
    return sorted_posts


def save_data(src, content):
    posts = load_data()
    dict = {"pic": src, "content": content}
    posts.append(dict)
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii= False)


def check_extension(name):
    extension = name.split(".")[1]
    if extension not in allowed_extensions:
        logging.error("Формат файла не поддерживается")
        raise NotAllowedExtension(f"File with {extension}-extension is not allowed ")

# pprint(load_data())
# pprint(search_posts("они"))

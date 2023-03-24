from flask import Blueprint, render_template, request
import logging
import functions

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename="basic.log")

@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/uploaded", methods=['POST'])
def uploaded_page():
    try:
        content = request.form['content']
        picture = request.files.get("picture")
        filename = picture.filename
        try:
            functions.check_extension(filename)
        except functions.NotAllowedExtension:
            return f"Данный формат файла не поддерживается"
        except IndexError:
            logging.exception("Ошибка загрузки")
            return f"Файл не отправлен"

        picture.save(f"./uploads/{filename}")
        pic_path = f"/uploads/{filename}"
        functions.save_data(pic_path, content)
        return render_template("post_uploaded.html", content=content, pic_path=pic_path)
    except PermissionError:
        logging.exception("Ошибка загрузки")
        return "Ошибка загрузки"

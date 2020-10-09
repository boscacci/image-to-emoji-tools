import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "."
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

application = Flask(__name__)
application.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@application.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(
                application.config["UPLOAD_FOLDER"], "current_image"
            )
            file.save(filepath)
            from make_preds import make_pred

            return str(make_pred(filepath))
            # return redirect(url_for("uploaded_file", filename=filename))
    return """
    <!doctype html>
    <title>Upload Image to Emojify</title>
    <h1>Upload Image to Emojify</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()
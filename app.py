from flask import Flask, render_template, request, url_for, redirect
import os
from merger_fg_with_template import transformImageUpload

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "userUploadLOGO"

@app.route("/")
def main():
    return render_template("fileUpload.html")

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(upload_path)
        transformImageUpload(upload_path, "formatTemplates/1.PNG", "static/generatedTemplates/output.png")
        transformImageUpload(upload_path, "formatTemplates/2.PNG", "static/generatedTemplates/output2.png")
        transformImageUpload(upload_path, "formatTemplates/3.PNG", "static/generatedTemplates/output3.png")
        transformImageUpload(upload_path, "formatTemplates/4.PNG", "static/generatedTemplates/output4.png")
        transformImageUpload(upload_path, "formatTemplates/5.PNG", "static/generatedTemplates/output5.png")
        transformImageUpload(upload_path, "formatTemplates/6.PNG", "static/generatedTemplates/output6.png")
        transformImageUpload(upload_path, "formatTemplates/7.PNG", "static/generatedTemplates/output7.png")
        return redirect("/show")

@app.route("/show")
def show():
    return render_template("displayImage.html", image_url="/generatedTemplates/output.png")



if __name__=="__main__":
    app.run(host='0.0.0.0')
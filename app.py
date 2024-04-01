from flask import Flask, render_template, request, url_for, redirect
import os
from placingNoBG_onTemplates import overlay_rgba_on_rgb
from gpt_api import comp

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "userUploadLOGO"
output_file_name = []


@app.route("/")
def main():
    return render_template("fileUpload.html")

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        textarea = request.form.get("textarea")
        print(textarea)
        filename = file.filename
        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(upload_path)
        templatePath = "formatTemplates"
        a=1
        MaxToken=1000
        result = comp(textarea, MaxToken, outputs=1)[0]
        
        for i in os.listdir(templatePath):
            outputFolder = os.path.join("static/generatedTemplates", f"output{a}.png")
            output_file_name.append(f"output{a}.png")
            template = os.path.join(templatePath, i)
            overlay_rgba_on_rgb(upload_path, template, outputFolder, x=5, y=5)
            a+=1

        return render_template("displayImage.html", images=output_file_name, res=f"Generated string type has max length of {MaxToken}: {result}")

@app.route("/show")
def show():
    return render_template("displayImage.html", images=output_file_name)



if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

appSName = "Aplikasi Daftar Antrian"
appName = f"{appSName} - by Amen Togu [50423150]"
appDesc = f"\"{appName}\" yang diperuntukkan untuk Project Informatika Kesehatan. Aplikasi ini berguna untuk membuat daftar antrian untuk fasilitas kesehatan seperti Puskesmas, Rumah Sakit, dan fasilitas kesehatan lainnya."


@app.route("/")
def home():
    return render_template('home.html', appName=appName, appDesc=appDesc, appSName=appSName)


@app.route("/sayHI/<name>")
def sayHI(name):
    return f"<h1> Hi, {escape(name)}! </h1>"

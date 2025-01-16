from flask import Flask, render_template, request, redirect, session
from markupsafe import escape
from time import time
import string
import random
import datetime

app = Flask(__name__)

appSName = "Pendaftaran Kesehatan"
appAuthor = "Kelompok 4 - 2IA07 - Universitas Gunadarma - 2024/2025"
appDesc = f"\"{appSName}\" ini adalah sebuah Aplikasi yang diperuntukkan untuk Project Informatika Kesehatan. Aplikasi ini berguna untuk membuat daftar antrian kesehatan dan pendaftaran untuk fasilitas kesehatan seperti Puskesmas, Rumah Sakit, dan fasilitas kesehatan lainnya."
faskesName = "RS Sentra Medika - Depok"  # Contoh

app.secret_key = '!@#$%^&'


# Default Rendered Template
def renderDefaultTemplate(page: str, pageName: str):
    return render_template(page, appAuthor=appAuthor, appDesc=appDesc, appSName=appSName, faskesName=faskesName, pageName=f"{pageName} -")

# Check Logged Session [! BLOM SELESAI]


def checkLogged():
    if 'id' in session:
        ""
    else:
        redirect("/")


@app.route("/")
def home():
    return renderDefaultTemplate('home.html', "Beranda")


@app.route("/daftar", methods=['POST', 'GET'])
def register():
    pageName = "Daftar Akun"
    namaDepanErr = ""
    namaBelakangErr = ""
    passwordErr = ""

    dataPerson = {"namaDepan": '', "namaBelakang": '', "email": ''}

    if request.method == "POST":

        if request.form['namaDepan'].isalpha():
            namaDepanErr = "is-valid"
        else:
            namaDepanErr = "is-invalid"

        if request.form['namaBelakang'].isalpha():
            namaBelakangErr = "is-valid"
        else:
            namaBelakangErr = "is-invalid"

        if request.form['new-password'] == request.form['password2']:
            passwordErr = "is-valid"
        else:
            passwordErr = "is-invalid"

        # Success
        if namaDepanErr == "is-valid" and namaBelakangErr == "is-valid" and passwordErr == "is-valid":

            chars = string.ascii_lowercase+string.ascii_uppercase+"@!/"+string.digits
            unixID = ''
            for i in range(28):
                unixID += random.choice(chars)
            print(unixID, request.form['email'])
            # session['id'] = unixID
            return redirect("/dashboard")
        else:
            dataPerson["namaDepan"] = request.form['namaDepan']
            dataPerson["namaBelakang"] = request.form['namaBelakang']
            dataPerson["email"] = request.form['email']

    return render_template("register.html", appAuthor=appAuthor, appDesc=appDesc, appSName=appSName, faskesName=faskesName, pageName=pageName, namaDepanErr=namaDepanErr, namaBelakangErr=namaBelakangErr, passwordErr=passwordErr, namaDepan=dataPerson['namaDepan'], namaBelakang=dataPerson["namaBelakang"], email=dataPerson["email"])


if __name__ == '__main__':
    app.run(debug=True)

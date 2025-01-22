from flask import Flask, render_template, request, redirect, session
from time import time
import string
import random
import datetime
import os

from core.session import checkSessionFile, addSession
from core.userAuth import checkAccountFile, addAccount, checkAccountEmail

app = Flask(__name__)

appSName = "Pendaftaran Kesehatan"
appAuthor = "Kelompok 4 - 2IA07 - Universitas Gunadarma - 2024/2025"
# appDesc = f"\"{appSName}\" ini adalah sebuah Aplikasi yang diperuntukkan untuk Project Informatika Kesehatan. Aplikasi ini berguna untuk membuat daftar antrian kesehatan dan pendaftaran untuk fasilitas kesehatan seperti Puskesmas, Rumah Sakit, dan fasilitas kesehatan lainnya."
appDesc = f"Di Sentra Medika Hospital Group (SMHG), kami memberikan pelayanan yang ramah, cepat, informatif, teliti dan mengutamakan keselamatan pasien. SMHG berkomitmen untuk mengedepankan kualitas & mutu pelayanan sesuai Standar Nasional Akreditasi Rumah Sakit yang kami dapatkan dengan PARIPURNA. Kami siap memberikan pelayanan dengan sepenuh hati untuk kesembuhan dan kenyamanan pasien yang datang ke Sentra Medika Hospital Group."
faskesName = "RS Sentra Medika - Depok"  # Contoh

app.secret_key = '!@#$%^&'


# Default Rendered Template
def renderDefaultTemplate(page: str, pageName: str, errorLogin=False):
    loginCheck = False
    if checkSession():
        loginCheck = True

    return render_template(page, appAuthor=appAuthor, appDesc=appDesc, appSName=appSName, faskesName=faskesName, pageName=f"{pageName} -", loginCheck=loginCheck, errorLogin=errorLogin)


# Check Session
def checkSession():
    if "id" and "email" in session and (checkSessionFile(session['id'], session['email'])):
        return True
    else:
        False


# Create Session
def createSession(email):
    chars = string.ascii_lowercase+string.ascii_uppercase+"@!/"+string.digits
    unixID = ''
    for i in range(28):
        unixID += random.choice(chars)

    session['email'] = request.form['email']
    session['id'] = unixID

    addSession(session['id'], session['email'])


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        if checkAccountFile(request.form['email'], request.form['password']):
            createSession(request.form['email'])
            return redirect("/dashboard")
        else:
            return renderDefaultTemplate('home.html', "Beranda", True)

    return renderDefaultTemplate('home.html', "Beranda")


@app.route("/daftar", methods=['POST', 'GET'])
def register():
    if checkSession():
        return redirect("/dashboard")

    pageName = "Daftar Akun"
    namaDepanErr = ""
    namaBelakangErr = ""
    passwordErr = ""
    emailErr = ""

    dataPerson = {"namaDepan": '', "namaBelakang": '', "email": ''}

    if request.method == "POST":
        if len(request.form) == 5:

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

            if checkAccountEmail(request.form['email']):
                emailErr = 'is-invalid'
            else:
                emailErr = 'is-valid'

            # Success
            if namaDepanErr == "is-valid" and namaBelakangErr == "is-valid" and passwordErr == "is-valid" and emailErr == 'is-valid':
                createSession(request.form['email'])
                addAccount(request.form['email'], request.form['new-password'],
                           f"{request.form['namaDepan']} {request.form['namaBelakang']}")

                return redirect("/dashboard")

            else:
                dataPerson["namaDepan"] = request.form['namaDepan']
                dataPerson["namaBelakang"] = request.form['namaBelakang']
                dataPerson["email"] = request.form['email']

        else:
            if request.method == "POST":
                if checkAccountFile(request.form['email'], request.form['password']):
                    createSession(request.form['email'])
                    return redirect("/dashboard")
                else:
                    return render_template("register.html", loginCheck=False, appAuthor=appAuthor, appDesc=appDesc, appSName=appSName, faskesName=faskesName, pageName=pageName, namaDepanErr=namaDepanErr, namaBelakangErr=namaBelakangErr, passwordErr=passwordErr, emailErr=emailErr, namaDepan=dataPerson['namaDepan'], namaBelakang=dataPerson["namaBelakang"], email=dataPerson["email"], errorLogin=True)

    return render_template("register.html", loginCheck=False, appAuthor=appAuthor, appDesc=appDesc, appSName=appSName, faskesName=faskesName, pageName=pageName, namaDepanErr=namaDepanErr, namaBelakangErr=namaBelakangErr, passwordErr=passwordErr, emailErr=emailErr, namaDepan=dataPerson['namaDepan'], namaBelakang=dataPerson["namaBelakang"], email=dataPerson["email"])


@app.route("/dashboard")
def dashboard():
    if checkSession():
        return f"Berhasil Masuk {session['email']}"
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)

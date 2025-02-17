from flask import Flask, render_template

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/iics/add')
def iics_add():
    return render_template("iics/add.html")

@app.route("iics", methods=['GET', 'POST'])
def iics():
    return render_template("iics.html")

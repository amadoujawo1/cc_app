from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
Bootstrap(app)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

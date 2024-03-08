from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>Contact Page</p>"

if __name__ == "__main__":
    app.run(debug=True)
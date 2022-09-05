#Creating Website using Flask Framework.
from flask import Flask, send_file, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug import secure_filename
from send_email import send_email


#App is Flask object. __name__ passed in to determine root path
app = Flask(__name__)
#Setting value of dictionary key so app knows where the database is
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
#Creating Database object
db = SQLAlchemy(app)

#Creating Database (Applying concepts from MS Access)
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    #Initialising attributes of Data class to Email and Height
    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

#Routing/Mapping URL to Python Function. Homepage is "/" root directory
@app.route("/")
#Home function for index html page
def index():
    #returning html template
    return render_template("index.html")

#Submission page that redirects user once data is submitted
@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        file.save(secure_filename("uploaded", file.filename))
        with open("uploaded" + file.filename, "a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html")

#Dunder name condition, means the indented code below will only run when this file is called directly
if __name__=="__main __":
    #Function to start/run the app
    app.run(debug=True)

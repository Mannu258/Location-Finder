from flask import Flask,render_template,request,redirect
import datetime
from datetime import datetime, timedelta

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


class Location(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String(200),nullable=False)
    ipAddress = db.Column(db.String(200),nullable=False)
    def get_ist_now():
        return datetime.utcnow() + timedelta(hours=5, minutes=30)
    created_at = db.Column(db.DateTime, default=get_ist_now)

class Crediantials(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    def __repr__(self) -> str:
        return f"{self.username}"


@app.route("/", methods=['GET'])
def index():
    if request.method == "GET":
        latitude = request.args.get('lat', type=float)
        longitude = request.args.get('lon', type=float)
        ip = request.args.get('ip', type=str)
        new_ip = f"{ip}"
        new_location = f"{latitude},{longitude}"
        location = Location(location = new_location,ipAddress=new_ip)
        db.session.add(location)
        db.session.commit()
    return render_template('index.html')


@app.route("/administrator",methods=['POST','GET'])
def Admin():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['password']
        admi = Crediantials.query.filter_by(username=username,password=password).first()
        if admi:
            location = Location.query.order_by(Location.ID.desc()).all()
            return render_template('details.html',location=location)

        else:
            return render_template('login.html')

    return render_template('login.html')



@app.route("/account",methods=['POST','GET'])
def Account():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['password']
        existing_user = Crediantials.query.filter_by(username=username).first()
        if existing_user:
            return "Account already exists. Please log in."
        
        if username:
            location = Crediantials(username = username,password=password)
            db.session.add(location)
            db.session.commit()
            return "Account Created Successfully"
    return render_template('account.html')


if __name__ == '__main__':
   app.run(debug=True ,port=8000)
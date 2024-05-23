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

@app.route("/secretadmin", methods=['GET'])
def details():
    location = Location.query.order_by(Location.ID.desc()).all()
    return render_template('details.html',location=location)

if __name__ == '__main__':
   app.run(debug=True ,port=8000)
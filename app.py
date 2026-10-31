import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-before-launch")
database_url = os.environ.get("DATABASE_URL", "sqlite:///cafe.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Hidden honeypot field helps filter basic automated spam.
        if request.form.get("website"):
            return redirect(url_for("home", _anchor="reviews"))
        name = (request.form.get("name") or "").strip()
        message = (request.form.get("message") or "").strip()
        try:
            rating = int(request.form.get("rating", "5"))
        except ValueError:
            rating = 0

        if not name or len(name) > 80:
            flash("Please enter your name (up to 80 characters).", "error")
        elif rating not in range(1, 6):
            flash("Please choose a rating from 1 to 5.", "error")
        elif len(message) < 8 or len(message) > 1000:
            flash("Your review should be between 8 and 1,000 characters.", "error")
        else:
            db.session.add(Review(name=name, rating=rating, message=message))
            db.session.commit()
            flash("Thank you! Your review has been published.", "success")
            return redirect(url_for("home", _anchor="reviews"))
    reviews = Review.query.order_by(Review.created_at.desc()).limit(30).all()
    return render_template("index.html", reviews=reviews)

@app.route("/health")
def health():
    return {"status": "ok"}

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)

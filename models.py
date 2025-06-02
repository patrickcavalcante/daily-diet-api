from database import db
from datetime import datetime

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255))
  datetime = db.Column(db.DateTime, default=datetime.utcnow)
  on_diet = db.Column(db.Boolean, nullable=False)

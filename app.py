from flask import Flask, request, jsonify
from models import Meal
from database import db
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
  db.create_all()

# Criar refeição
@app.route("/meals", methods=["POST"])
def create_meal():
  data = request.json
  try:
      meal = Meal(
        name=data["name"],
        description=data["description"],
        datetime=datetime.strptime(data["datetime"], "%Y-%m-%d %H:%M"),
        on_diet=data["on_diet"]
      )
      db.session.add(meal)
      db.session.commit()
      return jsonify({"id": meal.id}), 201
  except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 400

# Listar refeições
@app.route("/meals", methods=["GET"])
def get_meals():
  meals = Meal.query.all()
  return jsonify([{
    "id": m.id,
    "name": m.name,
    "description": m.description,
    "datetime": m.datetime.isoformat(),
    "on_diet": m.on_diet
  } for m in meals])

# Obter uma refeição
@app.route("/meals/<int:meal_id>", methods=["GET"])
def get_meal(meal_id):
  meal = Meal.query.get_or_404(meal_id)
  return jsonify({
    "id": meal.id,
    "name": meal.name,
    "description": meal.description,
    "datetime": meal.datetime.isoformat(),
    "on_diet": meal.on_diet
  })

# Atualizar refeição
@app.route("/meals/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
  meal = Meal.query.get_or_404(meal_id)
  data = request.json
  try:
    meal.name = data["name"]
    meal.description = data["description"]
    meal.datetime = datetime.strptime(data["datetime"], "%Y-%m-%d %H:%M")
    meal.on_diet = data["on_diet"]
    db.session.commit()
    return jsonify({"message": "Meal updated successfully"})
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 400

# Deletar refeição
@app.route("/meals/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
  meal = Meal.query.get_or_404(meal_id)
  db.session.delete(meal)
  db.session.commit()
  return jsonify({"message": "Meal deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)

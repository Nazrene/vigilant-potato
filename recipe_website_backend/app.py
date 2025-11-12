from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db , Recipe
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(app.instance_path, 'recipes.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def home():
    return "Welcome to Only Pans!"

@app.route("/recipes", methods=["GET" , "POST"])
def recipes():
    if request.method == "POST":
        data = request.get_json()
        
        if not data or "name" not in data or "ingredients" not in data: 
            return jsonify({"error" : "Name and ingredients are required"}), 400
        
        new_recipe = Recipe(
            name=data["name"],
            ingredients=data["ingredients"],
            instructions=data.get("instructions" , "")
        )

        db.session.add(new_recipe)
        db.session.commit()

        return jsonify({
            "message":f"Recipe '{new_recipe.name}' added successfully!" ,
            "recipe": {
                "id":new_recipe.id,
                "name":new_recipe.name,
                "ingredients":new_recipe.ingredients,
                "instructions":new_recipe.instructions
            }
        }),201
    
    recipes = Recipe.query.all()
    recipes_list = [
        {
            "id": recipe.id,
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions
        }
        for recipe in recipes
    ]

    return jsonify(recipes_list), 200

@app.route("/recipes/<recipe_name>", methods=["GET", "PUT", "DELETE"])
def recipe_detail(recipe_name):
    recipe = Recipe.query.filter_by(name=recipe_name).first()

    if not recipe:
        return jsonify({"error": "Recipe not found"}) , 404
    
    if request.method == "GET":
        return jsonify({
            "id": recipe.id,
            "name": recipe.name ,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions
    }) , 200 
    
    if request.method == "PUT":
        data = request.get_json()
        recipe.name = data.get("name", recipe.name)
        recipe.ingredients = data.get("ingredients", recipe.ingredients)
        recipe.instructions = data.get("instructions", recipe.instructions)
        db.session.commit()

        return jsonify({
            "message": f"Recipe '{recipe.name}' updated successfully!",
            "recipe": {
                "id": recipe.id,
                "name": recipe.name,
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions
            }
        }) ,200
    
    if request.method == "DELETE":
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({"message": f"Recipe'{recipe_name}' deleted successfully!"}) ,200
    
from models import User, Recipe, Review
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask , request , jsonify

app = Flask(__name__)

recipes_list = [
    {"name": "spaghetti", "ingredients": ["pasta", "tomato sauce", "cheese"]},
    {"name": "pancakes", "ingredients": ["flour", "milk", "eggs", "sugar"]}
]

@app.route("/")
def home():
    return "Welcome to Only Pans!"

@app.route("/recipes", methods=["GET" , "POST"])
def recipes():
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"message": "Recipe received", "recipe": data}), 201
    
    return "Here is a list of all recipes"

@app.route("/recipes/<recipe_name>", methods=["GET"])
def recipe(recipe_name):
    for recipe in recipes_list:
        if recipe ["name"].lower() ==  recipe_name.lower():
            return jsonify(recipe)
    return jsonify({"error":"Recipe not found"}) , 404

@app.route("/add-recipe", methods=["POST"])
def new_recipe():
    data = request.get_json
    return jsonify({
        "message": f"Recipe '{data['name']}' added suucessfully!" ,
        "recipe": data
    }) , 201

@app.route("/recipes/<recipe_name>", methods=["PUT"])
def edit_recipe(recipe_name):
    data = request.get_json()
    for recipe in recipes_list:
        if recipe["name"].lower() == recipe_name.lower():
            recipe.update(data)
            return jsonify({"message": "Recipe updated!", "updated_recipe": recipe}), 200
    return jsonify({"error": "Recipe not found"}) , 404
        

@app.route("/recipes/<recipe_name>", methods=["DELETE"])
def delete_recipe(recipe_name):
    global recipes_list 
    for recipe in recipes_list:
        if recipe["name"].lower() == recipe_name.lower():
            recipes_list.remove(recipe)
            return jsonify({"message": f"Recipe '{recipe_name}' deleted successfully!"}), 200
    
    return jsonify({"error": "Recipe not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

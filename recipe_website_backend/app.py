from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Only Pans!"

@app.route("/recipes", methods=["GET" , "POST"])
def recipes():
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"message": "Recipe received", "recipe": data}), 201
    
    return "Here is a list of all recipes"

@app.route("/recipe/<recipe_name>", methods=["GET"])
def recipe(recipe_name):
    return f"Showing details for {recipe_name} recipe"

@app.route("/add-recipe", methods=["POST"])
def new_recipe():
    data = request.get_json
    return jsonify({
        "message": f"Recipe '{data['name']}' added suucessfully!" ,
        "recipe": data
    }) , 201

@app.route("/edit-recipe/<recipe_name>", methods=["PUT"])
def edit_recipe(recipe_name):
    data = request.json
    return f"Admin:Updated {recipe_name} recipe to {data['name']}" , 200

@app.route("/delete-recipe/<recipe_name>", methods=["DELETE"])
def delete_recipe(recipe_name):
    return f"Admin:Deleted {recipe_name} recipe" , 200

if __name__ == "__main__":
    app.run(debug=True)

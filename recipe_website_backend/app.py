from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Only Pans!"

@app.route("/recipes")
def recipes():
    return "Here is a list of all recipes"

@app.route("/recipe/<recipe_name>")
def recipe(recipe_name):
    return f"Showing details for{recipe_name} recipe"

@app.route("/add-recipe")
def new_recipe():
    return f"Admin:Add a new recipe here!"

@app.route("/edit-recipe/<recipe_name>")
def edit_recipe(recipe_name):
    return f"Admin:Updating {recipe_name} recipe"

@app.route("/delete-recipe/<recipe_name>")
def delete_recipe(recipe_name):
    return f"Admin:Deleting {recipe_name} recipe"

if __name__ == "__main__":
    app.run(debug=True)

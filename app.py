from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_preferences = {}  
recipes = []  

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("preferences"))
    return render_template('index.html')  

@app.route("/preferences", methods=["GET", "POST"])
def preferences():
    if request.method == "POST":
        user_preferences["dietary_restrictions"] = request.form.get("dietary_restrictions", "")
        user_preferences["favorite_cuisine"] = request.form.get("favorite_cuisine", "")
        user_preferences["meals_per_week"] = request.form.get("meals_per_week", "")

        return redirect(url_for("recipe"))
    return render_template('preferences.html', user_preferences=user_preferences)

@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    if request.method == "POST":
        recipe_name = request.form.get("recipe_name")
        ingredients = request.form.get("ingredients")
        if recipe_name and ingredients:
            recipes.append({"name": recipe_name, "ingredients": ingredients})
        return redirect(url_for("recipeplan"))
    return render_template('recipe.html')

@app.route("/recipeplan")
def recipeplan():
    return render_template('recipeplan.html', user_preferences=user_preferences, recipes=recipes)
    
if __name__ == "__main__":
    app.run(debug=True)

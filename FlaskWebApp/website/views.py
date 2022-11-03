from flask import Blueprint, render_template
from flask import Flask, render_template, request, flash
from .forms import AddRecipe
from . import db
from .models import *

views = Blueprint('views', __name__) #same name as file


#HOMEPAGE
@views.route('/') #homepage decorator

def home(): #it will run only on this page
    return render_template("home.html")

#ADD RECIPE TO DATABASE PAGE
@views.route('/addRecipe', methods=['GET','POST'])
##Form function to add
def AddRecipes():
    
    form = AddRecipe(csrf_enabled=True)
    if form.validate_on_submit():
        
        recipe_name = request.form['recipe_name']
        recipe_notes = request.form['recipe_notes']
        difficulty = request.form['difficulty']
        cuisine = request.form['cuisine']
        course = request.form['course']
        diet = request.form['diet']
        recipe_ingredient = request.form['recipe_ingredient']
        recipe_instructions = request.form['recipe_instructions']

       
        record = Recipe(recipe_name,recipe_notes,difficulty,cuisine,course,diet,recipe_instructions,recipe_ingredient)

        db.session.add(record)
        db.session.commit()
    
    return render_template('AddRecipe.html',form=form, title= "Add recipe to database")
    

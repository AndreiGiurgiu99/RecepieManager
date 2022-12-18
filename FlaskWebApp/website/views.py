from flask import Blueprint, render_template, url_for,redirect
from flask import  render_template, request, flash
from .forms import AddRecipe
from . import db
from .models import *
import re


views = Blueprint('views', __name__) #same name as file


#HOMEPAGE
@views.route('/') #homepage decorator

def home(): #it will run only on this page
    return render_template("home.html")

#ADD RECIPE TO DATABASE PAGE
@views.route('/addRecipe', methods=['GET','POST'])

##FORM FUNCTION TO ADD RECIPE TO DATABASE
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

        ### Saves image in download folder /static/images/recipeImages ###
        form.recipe_image.data.save(f"FlaskWebApp/website/static/images/recipeImages/{recipe_name}.jpg")
        
        record = Recipe(recipe_name,recipe_notes,difficulty,cuisine,course,diet,recipe_ingredient,recipe_instructions)

        db.session.add(record)
        db.session.commit()
        
        ####THIS RETURN EMPTIES THE FORM BY REDIRECTING TO THE SAME PAGE###
        return redirect(url_for("views.AddRecipes"))
        
      
      
    return render_template('AddRecipe.html',form=form)
        
@views.route('/RecipeDatabase')

def GetData():
    recipes = Recipe.query.all()
    return render_template('RecipeDatabase.html', recipes=recipes)


### Dynamic page creation for each recipe in the database ###
@views.route('/Recipe/<recipeid>', methods = ['GET'])
def ShowRecipe(recipeid):
    
    ###Query to return the database entry that has the name of the page###
    recipedata = Recipe.query.filter_by(recipe_name=recipeid).first()

    ###Set the filepath for the image associated with the recipe saved in recipeImages in the static folder###
    recipeimage = url_for('static', filename=f'/images/recipeImages/{str(recipedata.recipe_name)}.jpg')
    
    recipeingredients = recipedata.ingredients_id.split(",")

    ### REGEX CONDITION TO SPLIT STRING ON ONE OR MORE /n ###
    regexCondition = r"(?:\r?\n){2,}"
    recipeinstructions = re.split(regexCondition,recipedata.instructions_id.strip())
    return render_template('RecipeTemplate.html', recipeid=recipeid,recipedata=recipedata,recipeimage=recipeimage,recipeingredients=recipeingredients,recipeinstructions=recipeinstructions)

@views.route('/Delete/<deletedRecipe>',methods = ['GET','POST'])
def DeleteRow(deletedRecipe):

    ###Creates a temporary url for the DB Entry that is going to be deleted###
    ###Then commits the change in the DB so the entry will be deleted from the DB and the page aswell###
    rowDel = Recipe.query.filter_by(recipe_name=deletedRecipe).first_or_404()

    db.session.delete(rowDel)
    db.session.commit() 
    return redirect('/RecipeDatabase')

@views.route('/Edit/<editRecipe>',methods = ['GET','POST'])
def EditRow(editRecipe):

    ### SAME AS DELETE FUNCTION GETS THE ELEMENT BY RECIPE NAME###
    recipeToEdit = Recipe.query.filter_by(recipe_name = editRecipe).first_or_404()

    ### CREATES THE FORM USED TO ADD RECIPE ###
    form = AddRecipe(request.form, obj = recipeToEdit,csrf_enabled=True)
    
    ### POPULATES THE ROWS USING THE EXISTING DATA FROM THE DATABASE###
    if request.method == 'GET':
        
        form.difficulty.data = recipeToEdit.difficulties_id
        form.recipe_ingredient.data = recipeToEdit.ingredients_id
        form.recipe_instructions.data = recipeToEdit.instructions_id
        form.cuisine.data = recipeToEdit.cuisines_id
        form.course.data = recipeToEdit.courses_id
    
    ### ON POST REQUEST IT UPDATES THE DATA FROM THE DATABASE WITH THE NEW DATA###
    if request.method == 'POST' and form.validate_on_submit():
        
        
        recipeToEdit.difficulties_id = form.difficulty.data
        recipeToEdit.cuisines_id = form.cuisine.data
        recipeToEdit.courses_id = form.course.data
        recipeToEdit.instructions_id = form.recipe_instructions.data
        recipeToEdit.ingredients_id = form.recipe_ingredient.data

        ### CHANGES THE NAME AND NOTES OF THE RECIPE###
        form.populate_obj(recipeToEdit)
        db.session.add(recipeToEdit)
        db.session.commit()
        return redirect('/RecipeDatabase')

    return render_template('EditRecipe.html', recipeToEdit = recipeToEdit, editRecipe=editRecipe, form=form)
from . import db
from sqlalchemy.orm import declarative_base, relationship


######### RECIPE TABLE MODELS AND RELATIONS ##################

class Recipe(db.Model):
    __tablename__ = 'Recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.Text, unique=False)
    recipe_notes = db.Column(db.Text, unique=False)
    difficulties_id = db.Column(db.Text, unique=False)
    cuisines_id = db.Column(db.Text, unique=False)
    courses_id = db.Column(db.Text, unique=False)
    diets_id = db.Column(db.Text, unique=False)
    instructions_id = db.Column(db.Text, unique=False)
    ingredients_id = db.Column(db.Text, unique = False)
    

    def __init__(self, recipe_name, recipe_notes, difficulties_id, cuisines_id, courses_id, diets_id, instructions_id, ingredients_id):
        self.recipe_name = recipe_name
        self.recipe_notes = recipe_notes
        self.difficulties_id = difficulties_id
        self.cuisines_id = cuisines_id
        self.courses_id = courses_id
        self.diets_id = diets_id
        self.instructions_id = instructions_id
        self.ingredients_id = ingredients_id




    


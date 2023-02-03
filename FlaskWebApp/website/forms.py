from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, HiddenField, StringField, TextAreaField, FileField
from wtforms.validators import InputRequired, Length, Regexp


class AddRecipe(FlaskForm):
    id_field = HiddenField()
    recipe_name = StringField('Recipe Name', [InputRequired(),
        Regexp(r'^[A-Za-z\s]+$', message="Invalid recipe name"),
        Length(min=2, max=30, message=f"Invalid length it should be between {min} and {max}")] )
    recipe_notes = StringField('Add notes for the recipe',[InputRequired(),
        Regexp(r'[A-Za-z0-9_.-]*', message="Invalid charachters used")])
    difficulty = SelectField('Select recipe difficulty',
                                choices=['easy','medium','hard'])
    cuisine = SelectField('Select cuisine',
                                choices=['French','Italian','Greek','Romanian','Turkish','Lebanese','American','African','Mexican','Chinese','Thai','Japanese','Indian'])
    course = SelectField('Select course',
                                choices=['Appetizer','Main','Sidedish','Sandwiches','Dessert','Soups/Stews','Bread','Pastry','Snack','Drinks'])
    diet =  SelectField('Select diets',
                                choices=['No Diet','Low sugar','High protein','High carbs','Gluten-free','Vegetarian','Vegan'])
    recipe_ingredient = TextAreaField('Add ingredient/quantity/measurments')
    recipe_instructions = TextAreaField('Add instructions')
    recipe_image = FileField()

    update = HiddenField()
    submit = SubmitField('Submit')


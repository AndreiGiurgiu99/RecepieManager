from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange


class AddRecipe(FlaskForm):
    id_field = HiddenField()
    recipe_name = StringField('Recipe Name')
    recipe_notes = StringField('Add notes for the recipe')
    difficulty = SelectField('Select recipe difficulty',
                                choices=['easy','medium','hard'])
    cuisine = SelectField('Select cuisine',
                                choices=['indian','asian','european'])
    course = SelectField('Select course',
                                choices=["appetizer", "main", "dessert", "drinks", "soups / stews","snack"])
    diet =  SelectField('Select diets',
                                choices=['low sugar','high protein','high carbs','gluten-free','vegetarian','vegan'])
    recipe_ingredient = TextAreaField('Add ingredient/quantity/measurments')
    recipe_instructions = StringField('Add instructions')

    update = HiddenField()
    submit = SubmitField('Submit')


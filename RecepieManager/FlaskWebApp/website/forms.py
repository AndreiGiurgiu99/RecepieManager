from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, HiddenField, StringField, TextAreaField, FileField
from wtforms.validators import InputRequired, Length, Regexp


class AddRecipe(FlaskForm):
    id_field = HiddenField()
    recipe_name = StringField('Recipe Name', [InputRequired(),
        Regexp(r'^[A-Za-z\s]+$', message="Invalid recipe name"),
        Length(min=2, max=25, message=f"Invalid length it should be between {min} and {max}")] )
    recipe_notes = StringField('Add notes for the recipe',[InputRequired(),
        Regexp(r'^[a-zA-Z0-9_.-]*$', message="Invalid charachters used")])
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
    recipe_image = FileField()

    update = HiddenField()
    submit = SubmitField('Submit')


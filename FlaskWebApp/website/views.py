from flask import Blueprint, render_template

views = Blueprint('views', __name__) #same name as file

@views.route('/') #homepage decorator

def home(): #it will run only on this page
    return render_template("home.html")
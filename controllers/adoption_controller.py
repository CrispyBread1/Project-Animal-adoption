from flask import render_template, Blueprint, redirect, request

from repositories import animal_repository
from repositories import shelter_repository
from models.animal import Animal

adoption_blueprint = Blueprint("animals", __name__)

@adoption_blueprint.route("/animals")
def index():
    animals = animal_repository.select_all()
    return render_template("pages/index.html", all_animals = animals)

@adoption_blueprint.route("/shelter")
def index_shelter():
    shelters = shelter_repository.select_all()
    return render_template("pages/index_shelters.html", all_shelters = shelters)

@adoption_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    return render_template("pages/more_information.html", animal = animal)

@adoption_blueprint.route("/shelter/<id>")
def show_shelter(id):
    animals = animal_repository.select_all()
    shelter = shelter_repository.select(id)
    return render_template("pages/shelter.html", all_animals = animals, shelter = shelter)

@adoption_blueprint.route("/animals/<id>/delete", method =["POST"])
def destroy(id):
    animal_repository.delete(id)
    return redirect("/animals")

@adoption_blueprint.route("/animals/new")
def new():
    all_shelters = shelter_repository.select_all()
    return render_template("pages/new.html", all_shelters = all_shelters)

@adoption_blueprint.route("/animals", methods=["POST"])
def create():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    description = request.form['description']
    shelter_id = request.form['shelter_id']
    shelter = shelter_repository.select(shelter_id)
    animal = Animal(name, dob, type, description, shelter)
    animal_repository.save(animal)
    return redirect('/animals')
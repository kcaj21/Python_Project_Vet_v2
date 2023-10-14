from flask import Flask, render_template, request, redirect, Blueprint
from models.animal import Animal
from models.vet import Vet
from repositories import animal_repository, vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)

@animals_blueprint.route("/animals/add", methods = ['GET'])
def new_animal():
    vets = vet_repository.select_all()
    return render_template("animals/add.html", all_vets = vets)

@animals_blueprint.route("/animals", methods = ['POST'])
def add_animal():
    name = request.form["name"]
    type = request.form["type"]
    contact_details = request.form["contact_details"]
    date_of_birth = request.form["date_of_birth"]
    treatment_notes = request.form["treatment_notes"]
    check_in_date = request.form["check_in_date"]
    check_out_date = request.form["check_out_date"]
    vet_id = request.form["vet_id"]

    vet = vet_repository.select(vet_id)
    animal = Animal(name, type, contact_details, date_of_birth, treatment_notes, check_in_date, check_out_date, vet)

    animal_repository.add_animal(animal)
    return redirect ("/animals")

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/show.html', animal = animal)

@animals_blueprint.route("/animals/<id>/update", methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    vets = vet_repository.select_all()
    return render_template("animals/update.html", animal = animal, all_vets = vets)

@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form["name"]
    type = request.form["type"]
    contact_details = request.form["contact_details"]
    date_of_birth = request.form["date_of_birth"]
    treatment_notes = request.form["treatment_notes"]
    check_in_date = request.form["check_in_date"]
    check_out_date = request.form["check_out_date"]
    vet_id = request.form["vet_id"]

    vet = vet_repository.select(vet_id)
    animal = Animal(name, type, contact_details, date_of_birth, treatment_notes, check_in_date, check_out_date, vet, id)

    animal_repository.update(animal)
    return redirect ("/animals")

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect ("/animals")
    
@animals_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("animals/vets.html", all_vets = vets)   








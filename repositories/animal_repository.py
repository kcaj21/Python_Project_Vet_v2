from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository


def select_all():

    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    
    for row in results:
        vet = vet_repository.select(row["vet_id"])
        animal = Animal(row['name'], row['type'], row['contact_details'], row ['date_of_birth'], row['treatment_notes'], vet, row['id'])
        animals.append(animal)
    return animals

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def add_animal(animal):
    sql = "INSERT into animals (name, type, contact_details, date_of_birth, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.contact_details, animal.date_of_birth, animal.treatment_notes, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result["vet_id"])
        animal = Animal(result["name"], result["type"], result["contact_details"], result["date_of_birth"], result["treatment_notes"], vet, result["id"])
    return animal

def delete(id):
    sql = "DELETE FROM animals WHERE id = (%s)"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, type, contact_details, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = (%s)"
    values = [animal.name, animal.date_of_birth, animal.type, animal.contact_details, animal.treatment_notes, animal.vet.id, animal.id]
    run_sql(sql, values)
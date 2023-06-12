from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet

def select_all():

    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    
    for row in results:
        vet = Vet(row['name'], row['description'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result["name"], result["description"], result["id"])
    return vet


def add_vet(vet):
    sql = "INSERT into vets (name, description) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = (%s)"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (name, description) = (%s, %s) WHERE id = (%s)"
    values = [vet.name, vet.description, vet.id]
    run_sql(sql, values)
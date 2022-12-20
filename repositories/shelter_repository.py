from db.run_sql import run_sql

from models.animal import Animal
from models.shelter import Shelter

def save(shelter):
    sql = "INSERT INTO shelters (name, location, contact) VALUES (%s, %s, %s) RETURNING *"
    values = [shelter.name, shelter.location, shelter.contact]
    results = run_sql(sql, values)
    id = results['id']
    shelter.id = id 
    return shelter

def select_all():
    shelters = []

    sql = "SELECT * FROM shelters"
    results = run_sql(sql)

    for row in results:
        shelter = Shelter(row['name'], row['location'], row['contact']. row['id'])
        shelters.append(shelter)
    return shelters

def select(id):
    shelter = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        shelter = Shelter(result['name'], result['location'], result['contact']. result['id'])
    return shelter 

def delete_all():
    sql = "DELETE FROM shelters"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM shelters WHERE id = %s"
    values = id
    run_sql(sql, values)

def update(shelter):
    sql = "UPDATE shelters SET (name, location, contact) = (%s, %s) WHERE id = %s"
    values = [shelter.name, shelter.location, shelter.contact, shelter.id]
    run_sql(sql, values)



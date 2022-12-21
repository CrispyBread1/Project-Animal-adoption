from db.run_sql import run_sql

from models.animal import Animal
import repositories.shelter_repository as shelter_repository

def save(animal):
    sql = 'INSERT INTO animals (name, dob, type, description, img, shelter_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *'
    values = (animal.name, animal.dob, animal.type, animal.description, animal.img, animal.shelter.id)
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        shelter = shelter_repository.select(row['shelter_id'])
        animal = Animal(row['name'], row['dob'], row['type'], row['description'], row['img'],shelter, row['id'])
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        shelter = shelter_repository.select(result['shelter_id'])
        animal = Animal(result['name'], result['dob'], result['type'], result['description'], shelter, result['id'], result['img'])
    return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, dob, type, description, shelter_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.dob, animal.type, animal.description, animal.shelter.id, animal.id]
    run_sql(sql, values)

def animals_for_shelter(id):
    pass

def select_all_images():
    sql = "SELECT img FROM animals"
    images = run_sql(sql)
    return images

    
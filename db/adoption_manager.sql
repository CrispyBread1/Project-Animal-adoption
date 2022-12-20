DROP TABLE IF EXISTS: shelter;
DROP TABLE IF EXISTS: animals;

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    contact VARCHAR(255),
    description VARCHAR(255),   
);

CREATE TABLE shelters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    contact VARCHAR(255),
    animal_id INT NOT NULL REFERENCES animals(id)
);

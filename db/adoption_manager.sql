DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS shelters;


CREATE TABLE shelters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    description VARCHAR(255),   
    shelter_id INT NOT NULL REFERENCES shelters(id)
);

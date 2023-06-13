DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS animals;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    contact_details VARCHAR(13),
    date_of_birth DATE,
    treatment_notes VARCHAR(255),
    check_in_date DATE,
    check_out_date DATE,
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);

INSERT INTO vets (name, description) VALUES ('Dr Ink', 'More likely to anaesthetise themselves before the animal');
-- INSERT INTO vets (name, description) VALUES ('Dr Robotnik', 'A miserly, sadistic man. Absolutely will not treat headgehogs.');
-- INSERT INTO vets (name, description) VALUES ('Dr Zoidberg', 'Easily startled and fiendishly hungry.');
-- INSERT INTO vets (name, description) VALUES ('Dr Dolittle', 'An actual vet.');
-- INSERT INTO vets (name, description) VALUES ('Dr Dre', 'Great with doggs.');



INSERT INTO animals (name, type, contact_details, date_of_birth, treatment_notes, check_in_date, check_out_date, vet_id) VALUES ('Barney', 'Dinosaur', '+447123456789', '1992-04-06', 'Prosthetic tail insertion', '2023-04-06', '2023-05-07', 1);


-- UPDATE animals SET contact_details = 'none' WHERE name = 'Barney';
-- UPDATE vets SET description = 'none' WHERE name = 'Dr Ink';


-- DELETE FROM animals WHERE name = 'Barney';
DELETE FROM vets WHERE id = 5;
-- DELETE FROM vets WHERE id = 6;
SELECT * FROM vets;

SELECT * FROM animals;
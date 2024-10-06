CREATE TABLE films (
  	name TEXT,
  	release_year integer
  	
);
  
INSERT INTO films (name, release_year)
VALUES ('Transformers',2007),('The matrix', 1999), ('Pacific War', 2010);  
 
SELECT * FROM films;


selecting films by release_year 
SELECT * FROM films WHERE release_year = 2007; 
SELECT * FROM films WHERE release_year > 2000; 

-- Adding new columns to existing table. BIGINT for high integer numbers 
ALTER TABLE films
ADD COLUMN runtime INTEGER,
ADD COLUMN category TEXT,
ADD COLUMN rating numeric(3,1), -- 3 digits, 1 after dot
ADD COLUMN box_office BIGINT;

Updating existing rows with new information for NULL values 
UPDATE films
SET runtime = 136, category = 'Action', rating = 8.7 , box_office = 463517383
WHERE name = 'The matrix'; 

adding unique constraint to prevent duplicate movie names
ALTER TABLE films
ADD CONSTRAINT unique_name UNIQUE (name); 

ALTER TABLE films
ADD CONSTRAINT release_year UNIQUE (release_year);

INSERT INTO films (name,release_year)
VALUES ('deneme',1999);

-- after running last code we get : duplicate key value violates unique constraint "release_year" 




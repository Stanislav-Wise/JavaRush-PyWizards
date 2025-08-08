-- CREATE TABLE review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL,
-- 	customer_id INTEGER NOT NULL,
-- 	review_text TEXT,
-- 	rating NUMERIC(2,1) NOT NULL,
-- 	review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	is_active BOOLEAN DEFAULT TRUE
-- );

-- CREATE TABLE test_table (
-- 	id SERIAL PRIMARY KEY,
-- 	text TEXT,
-- 	date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	is_active BOOLEAN DEFAULT TRUE
-- );

-- SMALLINT
-- BIGINT
-- DATE
-- CHAR(n)
-- VARCHAR(n)
-- FOREIGN KEY


-- CREATE TABLE votes (
-- 	votes_id INTEGER,
-- 	el_id INTEGER,
-- 	choice TEXT,
-- 	PRIMARY KEY (votes_id, el_id)
-- )


-- CREATE TABLE review_new (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL,
-- 	customer_id INTEGER NOT NULL,
-- 	review_text TEXT UNIQUE,
-- 	rating NUMERIC(2,1) NOT NULL,
-- 	review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	is_active BOOLEAN DEFAULT TRUE,
-- 	CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES film(film_id),
-- 	CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer(customer_id)

-- );


CREATE TABLE test_two (
	customer_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	city TEXT DEFAULT 'Москва',
	age INTEGER CHECK (age >= 18),
	status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive'))
);
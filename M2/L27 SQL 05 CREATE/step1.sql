-- CREATE TABLE votes (
-- 	votes_id INTEGER,
-- 	el_id INTEGER,
-- 	choice TEXT,
-- 	PRIMARY KEY (votes_id, el_id)
-- )


-- CREATE TABLE test_two (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL,
-- 	city TEXT DEFAULT 'Москва',
-- 	age INTEGER CHECK (age >= 18),
-- 	status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive'))
-- );

-- ALTER TABLE test_two
-- ADD COLUMN phone TEXT;

-- ALTER TABLE test_two
-- ADD COLUMN is_verified BOOLEAN DEFAULT FALSE NOT NULL;

-- ALTER TABLE test_two
-- DROP COLUMN phone;


-- ALTER TABLE test_two
-- RENAME COLUMN status TO is_active;


-- ALTER TABLE test_two
-- ALTER COLUMN name TYPE TEXT;

-- ALTER TABLE test_two
-- ALTER COLUMN name TYPE VARCHAR(20);


-- ALTER TABLE test_two
-- ALTER COLUMN city SET DEFAULT 'Сочи';

-- ALTER TABLE test_two
-- ALTER COLUMN city DROP DEFAULT;

-- ALTER TABLE test_two
-- ADD CONSTRAINT u_city UNIQUE (city);

-- ALTER TABLE test_two
-- DROP CONSTRAINT u_city;

ALTER TABLE test_two
RENAME TO test_five;
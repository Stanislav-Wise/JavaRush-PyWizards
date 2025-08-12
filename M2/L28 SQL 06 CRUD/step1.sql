-- DROP TABLE test_table;

-- DROP TABLE IF EXISTS test_five;

-- DROP TABLE IF EXISTS test_five, test2, test3;

-- DROP TABLE IF EXISTS test_five CASCADE;

-- INSERT INTO review_new (review_id, film_id, customer_id, review_text, rating, is_active)
-- VALUES (1, 1, 1, 'Отзыв', 3, true)

-- INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date)
-- VALUES (1, 'Bob', 'Ivanov', 'bob@mail.com', 3, 1, NOW());

-- INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date)
-- VALUES
-- 	(1, 'Petr', 'Petrov', 'ivan@mail.com', 3, 1, NOW()),
-- 	(1, 'Ivan', 'Sidorov', 'petr@mail.com', 3, 1, NOW());


-- CREATE TABLE customer_copy AS
-- SELECT * FROM customer WHERE false;

-- CREATE TABLE customer_copy1 AS
-- SELECT * FROM customer WHERE true;


-- INSERT INTO customer_copy (store_id, first_name, last_name, email, address_id, active, create_date)
-- SELECT store_id, first_name, last_name, email, address_id, active, create_date
-- FROM customer
-- WHERE store_id = 1;

-- CREATE TABLE customer_copy3 AS
-- SELECT * FROM customer WHERE false;

-- INSERT INTO customer_copy2 (store_id, first_name, last_name, email, address_id, active, create_date)
-- SELECT store_id, first_name, last_name, email, address_id, active, create_date
-- FROM customer
-- WHERE active = 1;

-- INSERT INTO customer_copy3 (store_id, first_name, last_name, email, address_id, active, create_date)
-- SELECT c.store_id, c.first_name, c.last_name, c.email, c.address_id, c.active, c.create_date
-- FROM customer c
-- JOIN address a ON c.address_id = a.address_id
-- WHERE a.city_id = 3;


-- INSERT INTO customer_copy3 (store_id, first_name, last_name, email, address_id, active, create_date)
-- VALUES (1, 'Bob', 'Ivanov', 'bob@mail.com', 3, 1, NOW())
-- RETURNING store_id, first_name;


-- UPDATE customer_copy3
-- SET email = 'b@gmail.com', last_name = 'Smith'
-- WHERE first_name = 'Bob';

-- UPDATE customer_copy3
-- SET address_id = address_id + 10
-- WHERE address_id < 100
-- RETURNING first_name, address_id;


-- DELETE FROM customer_copy
-- WHERE address_id > 10 AND first_name LIKE 'M%'
-- RETURNING first_name, address_id;

DELETE FROM customer
WHERE customer_id NOT IN (
	SELECT customer_id FROM rental
)
RETURNING first_name, customer_id;


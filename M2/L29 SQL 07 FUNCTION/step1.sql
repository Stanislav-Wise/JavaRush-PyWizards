-- SELECT c.customer_id, c.first_name, c.last_name
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- WHERE r.return_date - r.rental_date > INTERVAL '5 days';


-- WITH long_rental AS (
-- 	SELECT c.customer_id, c.first_name, c.last_name
-- 	FROM customer c
-- 	JOIN rental r ON c.customer_id = r.customer_id
-- 	WHERE r.return_date - r.rental_date > INTERVAL '5 days'
-- )
-- SELECT first_name
-- FROM long_rental
-- WHERE first_name LIKE 'A%';


-- WITH total_payments AS (
-- 	SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount) AS total
-- 	FROM customer c
-- 	JOIN payment p ON c.customer_id = p.customer_id
-- 	GROUP BY c.customer_id, c.first_name, c.last_name
-- )
-- SELECT *
-- FROM total_payments
-- WHERE total < 100;



-- WITH total_payments AS (
-- 	SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount) AS total
-- 	FROM customer c
-- 	JOIN payment p ON c.customer_id = p.customer_id
-- 	GROUP BY c.customer_id, c.first_name, c.last_name
-- ),

--  rental_counts AS (
-- 	SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rentals
-- 	FROM customer c
-- 	JOIN rental r ON c.customer_id = r.customer_id
-- 	GROUP BY c.customer_id, c.first_name, c.last_name
-- )

-- SELECT rc.customer_id, rc.first_name, rc.last_name, rentals, total
-- FROM total_payments tp
-- JOIN rental_counts rc ON tp.customer_id = rc.customer_id;

-- SELECT *
-- FROM (
-- 	SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.amount,
-- 		SUM(amount) OVER (),
-- 		AVG(amount) OVER () AS avg_amount
-- 	FROM payment p
-- ) t
-- WHERE amount > avg_amount;


-- SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.amount,
-- 		SUM(amount) OVER (PARTITION BY p.customer_id),
-- 		AVG(amount) OVER (PARTITION BY p.customer_id) AS avg_amount
-- FROM payment p


-- SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.amount,
-- 		ROW_NUMBER() OVER(ORDER BY amount DESC) AS r_nums
-- FROM payment p;


-- SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.payment_date,
-- 	 	SUM(amount) OVER(ORDER BY payment_date DESC) AS total
-- FROM payment p;


-- SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.payment_date,
-- 	 	SUM(amount) OVER(
-- 		 PARTITION BY p.customer_id
-- 		 ORDER BY p.payment_date DESC
-- 		 ) AS total,
-- 		 MAX(amount) OVER(ORDER BY payment_date DESC) AS max_amount
-- FROM payment p;




-- SELECT  p.payment_id,
-- 		p.customer_id,
-- 		p.payment_date,
-- 		amount,
-- 	 	SUM(
-- 			CASE
-- 				WHEN p.customer_id < 10 THEN amount
-- 				ELSE 0
-- 			END
-- 		) OVER(PARTITION BY p.customer_id) AS total
-- FROM payment p;


-- CREATE FUNCTION my_answer()
-- RETURNS integer
-- AS $$
-- 	SELECT 17;
-- $$ LANGUAGE SQL;

-- SELECT my_answer();


-- CREATE OR REPLACE FUNCTION my_answer2(num integer)
-- RETURNS integer
-- AS $$
-- 	SELECT num * 2;
-- $$ LANGUAGE SQL;

-- SELECT my_answer2(30);


-- CREATE OR REPLACE FUNCTION get_name(name_id integer)
-- RETURNS table
-- AS $$
-- 	SELECT first_name
-- 	FROM customer
-- 	WHERE customer_id = name_id;
-- $$ LANGUAGE SQL;
--
-- SELECT get_name(7);

DROP FUNCTION get_name(integer);

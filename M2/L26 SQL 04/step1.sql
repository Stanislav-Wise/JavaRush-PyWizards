-- SELECT COUNT(*) FROM payment;


-- SELECT COUNT(*) FROM customer;

-- SELECT COUNT(DISTINCT customer_id) FROM payment;

-- SELECT SUM(amount) FROM payment;

-- SELECT AVG(amount) FROM payment;

-- SELECT MIN(amount) FROM payment;

-- SELECT MAX(amount) FROM payment;

-- SELECT MIN(amount) AS min_amount, AVG(amount) AS avg_amount, MAX(amount) AS max_amount FROM payment;

-- SELECT DISTINCT city_id, district
-- FROM address
-- ORDER BY city_id;


-- SELECT customer_id, COUNT(*) AS num_payments
-- FROM payment
-- GROUP BY customer_id
-- ORDER BY num_payments;

-- SELECT release_year, COUNT(*) AS count_film
-- FROM film
-- GROUP BY release_year
-- ORDER BY release_year;

-- SELECT release_year
-- FROM film
-- ORDER BY release_year;


-- SELECT s.store_id, SUM(p.amount) AS store_res
-- FROM store s
-- JOIN customer c ON s.store_id = c.store_id
-- JOIN payment p ON c.customer_id = p.customer_id
-- GROUP BY s.store_id
-- ORDER BY store_res DESC;


-- SELECT customer_id, staff_id, COUNT(*) AS num_payments
-- FROM payment
-- GROUP BY customer_id, staff_id
-- ORDER BY customer_id;

-- SELECT customer_id, COUNT(*) AS num_payments
-- FROM payment
-- GROUP BY customer_id
-- ORDER BY customer_id;


-- SELECT customer_id, COUNT(*) AS num_payments
-- FROM payment
-- GROUP BY customer_id
-- HAVING COUNT(*) > 30
-- ORDER BY customer_id;

-- SELECT c.name,  COUNT(f.film_id) as num_films
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- GROUP BY c.name
-- HAVING  COUNT(f.film_id) > 50
-- ORDER BY num_films DESC;


-- SELECT
-- 	title,
-- 	length,
-- 	CASE
-- 		WHEN length > 120 THEN 'Полнометражный'
-- 		WHEN length < 80 THEN 'Короткометражный'
-- 		ELSE 'Обычный'
-- 	END AS film_type

-- FROM film;


-- SELECT
-- 	release_year,
-- 	COUNT(CASE WHEN length > 120 THEN 1 END) AS long_film,
-- 	COUNT(CASE WHEN length < 80 THEN 1 END) AS short_film,
-- 	COUNT(CASE WHEN length BETWEEN 80 AND 120 THEN 1 END) AS mid_film
-- FROM film
-- GROUP BY release_year
-- ORDER BY release_year;


-- SELECT
-- 	rating,
-- 	COUNT(CASE WHEN length > 120 THEN 1 END) AS long_film,
-- 	COUNT(CASE WHEN length < 80 THEN 1 END) AS short_film,
-- 	COUNT(CASE WHEN length BETWEEN 80 AND 120 THEN 1 END) AS mid_film
-- FROM film
-- GROUP BY rating
-- ORDER BY rating;


SELECT
	c.customer_id,
	c.first_name,
	c.last_name,
	(SELECT COUNT(*)
	FROM rental r
	WHERE r.customer_id = c.customer_id) AS rental_count
FROM customer c
ORDER BY rental_count DESC;


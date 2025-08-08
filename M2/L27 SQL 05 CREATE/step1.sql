-- SELECT customer_id, first_name, last_name
-- FROM customer
-- WHERE customer_id = (
-- 	SELECT customer_id
-- 	FROM payment
-- 	GROUP BY customer_id
-- 	ORDER BY SUM(amount) DESC
-- 	LIMIT 1
-- );


-- SELECT city_id, city
-- FROM city
-- WHERE city = 'Aurora';

-- SELECT c.customer_id, c.first_name, c.last_name
-- FROM customer c
-- JOIN address a ON c.address_id = a.address_id
-- WHERE a.city_id = (
-- 	SELECT city_id FROM city WHERE city = 'Aurora'
-- );

SELECT DISTINCT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.customer_id IN (
	SELECT c.customer_id
	FROM customer c
	JOIN address a ON c.address_id = a.address_id
	WHERE a.city_id = (
		SELECT city_id FROM city WHERE city = 'Aurora'
	)
);

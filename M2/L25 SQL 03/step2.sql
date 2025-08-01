-- SELECT *
-- FROM  customer c FULL JOIN rental r ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'M%'
-- ORDER BY r.rental_date DESC;


-- SELECT *
-- FROM  rental r JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.store_id = 1 AND r.inventory_id IN (
-- 	SELECT inventory_id FROM inventory
-- 	WHERE film_id IN (SELECT film_id FROM film WHERE rental_rate > 2.0)
-- );


SELECT r.rental_id, r.rental_date, c.first_name, c.last_name, f.title
FROM  customer c
JOIN rental r ON r.customer_id = c.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name LIKE 'M%'
ORDER BY r.rental_date DESC
LIMIT 10;
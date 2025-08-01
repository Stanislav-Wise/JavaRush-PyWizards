-- SELECT * FROM rental;
-- SELECT * FROM customer;

-- SELECT rental.rental_date
-- FROM rental INNER JOIN customer ON rental.customer_id = customer.customer_id;

-- SELECT rental.rental_id, rental.rental_date, customer.first_name, customer.last_name
-- FROM rental JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE customer.first_name LIKE 'M%'
-- ORDER BY rental.rental_date DESC;


-- SELECT r.rental_id, r.rental_date, c.first_name, c.last_name
-- FROM rental AS r JOIN customer AS c ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'M%'
-- ORDER BY r.rental_date DESC;


-- SELECT r.rental_id, r.rental_date, c.first_name, c.last_name
-- FROM rental r JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'M%'
-- ORDER BY r.rental_date DESC;


-- SELECT r.rental_id, r.rental_date, c.first_name, c.last_name
-- FROM  customer c LEFT JOIN rental r ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'M%'
-- ORDER BY r.rental_date DESC;


-- SELECT r.rental_id, r.rental_date, c.first_name, c.last_name
-- FROM  customer c RIGHT JOIN rental r ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'M%'
-- ORDER BY r.rental_date DESC;


SELECT r.rental_id, r.rental_date, c.first_name, c.last_name
FROM  customer c FULL OUTER JOIN rental r ON r.customer_id = c.customer_id
WHERE c.first_name LIKE 'M%'
ORDER BY r.rental_date DESC;

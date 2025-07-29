-- SELECT title, rating, rental_rate FROM film
-- WHERE rental_rate BETWEEN 2 AND 3;


-- SELECT title, rating, rental_rate FROM film
-- WHERE title LIKE '_c%';

SELECT * FROM film
WHERE description IS NOT NULL;
-- SELECT title, rating, rental_rate FROM film
-- WHERE (rental_rate < 1 OR rental_rate > 4) AND rating != 'PG-13'
-- ORDER BY rating DESC, rental_rate DESC, title
-- OFFSET 5
-- LIMIT 10;


SELECT title AS "Заголовок", rating AS Рейтинг, rental_rate FROM film
WHERE title LIKE 'C%' AND (rental_rate < 2 OR rental_rate > 4) AND rating IN ('PG-13', 'PG')
ORDER BY rating DESC, rental_rate DESC, title
OFFSET 5
LIMIT 10;
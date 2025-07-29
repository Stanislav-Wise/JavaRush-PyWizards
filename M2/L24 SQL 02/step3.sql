-- SELECT * FROM film
-- WHERE rating = 'PG-13' AND rental_rate > 4;


-- SELECT * FROM film
-- WHERE rating = 'PG-13' OR rental_rate > 4;


-- SELECT * FROM film
-- WHERE NOT rating = 'PG-13';


-- SELECT * FROM film
-- WHERE rating != 'PG-13';


-- SELECT * FROM film
-- WHERE (rental_rate < 1 OR rental_rate > 4) AND rating != 'PG-13';


SELECT title, rating FROM film
WHERE rating NOT IN ('PG-13', 'PG');

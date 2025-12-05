import sqlite3

from schemas.movie import Movie

conn = sqlite3.connect('temp.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM temp")
cursor.execute("SELECT * FROM temp")
cursor.execute("SELECT * FROM temp")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()



# movies = session.query(Movie).filter(Movie.genre == "Rock").all()


# genre = Genre(name='Комедия')
# INSERT INTO genres (name) VALUES ('Комедия');
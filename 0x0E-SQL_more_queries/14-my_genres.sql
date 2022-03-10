-- lists all genres of the show "Dexter"
SELECT genres.name
FROM tv_show_genres shows_genres
INNER JOIN tv_genres genres ON shows_genres.genre_id = genres.id
INNER JOIN tv_shows shows ON shows_genres.show_id = shows.id
WHERE shows.title = "Dexter"
ORDER BY genres.name;

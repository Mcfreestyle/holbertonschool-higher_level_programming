-- lists all shows, and all genres linked to that show,  from the database `hbtn_0d_tvshows`
SELECT shows.title, genres.name
FROM tv_show_genres shows_genres
	INNER JOIN tv_genres genres ON shows_genres.genre_id = genres.id
	RIGHT JOIN tv_shows shows ON shows_genres.show_id = shows.id
ORDER BY shows.title, genres.name;

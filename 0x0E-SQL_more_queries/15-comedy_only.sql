-- lists all Comedy shows in the database `hbtn_0d_tvshows`
SELECT shows.title
FROM tv_show_genres shows_genres
	INNER JOIN tv_genres genres ON shows_genres.genre_id = genres.id
	INNER JOIN tv_shows shows ON shows_genres.show_id = shows.id
WHERE genres.name = "Comedy"
ORDER BY shows.title;

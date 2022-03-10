-- lists all genres from `hbtn_0d_tvshows` with the number of shows linked to each
SELECT
	genres.name AS genre,
	COUNT(*) AS number_of_shows
FROM
	tv_show_genres genres_sh
INNER JOIN 
	tv_genres genres ON genres.id = genres_sh.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

-- lists all shows contained in `hbtn_0d_tvshows`that have at least one genre linked
SELECT title, genre_id
FROM tv_show_genres sg INNER JOIN tv_shows s
ON sg.show_id = s.id
ORDER BY title, genre_id;

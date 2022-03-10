-- lists all shows contained in the database `hbtn_0d_tvshows`
-- whether or not they belong to a gender in the gender table
SELECT title, genre_id
FROM tv_show_genres sg
RIGHT JOIN tv_shows s
ON sg.show_id = s.id
ORDER BY title, genre_id;

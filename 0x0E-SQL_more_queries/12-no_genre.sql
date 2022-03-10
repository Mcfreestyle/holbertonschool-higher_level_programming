-- lists all shows that don't belong to any genre in the `tv_genres` table contained in the database `hbtn_0d_tvshows`
SELECT title, genre_id
FROM tv_show_genres sg
RIGHT JOIN tv_shows s
ON sg.show_id = s.id
WHERE sg.genre_id IS NULL
ORDER BY title, genre_id;

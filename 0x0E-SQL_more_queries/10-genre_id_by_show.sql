-- the script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows 
INNER JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id AND tv_show_genres.genre_id>=1
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

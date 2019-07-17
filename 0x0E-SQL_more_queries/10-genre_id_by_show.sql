-- Importing from DB, selects and joins
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

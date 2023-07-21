-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
USE hbtn_0d_tvshows_rate
SELECT tv_genres.name SUM(tv_show_ratings.rate) AS rating
FROM tv_shows


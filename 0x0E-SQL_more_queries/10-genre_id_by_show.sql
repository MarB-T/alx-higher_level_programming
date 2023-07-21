-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one 
-- 	genre linked.
SELECT tvs.title, g.genre_id
  FROM tv_shows AS tvs
        INNER JOIN tv_show_genres AS g
	ON tvs.id = g.show_id
 ORDER BY tvs.title, g.genre_id;

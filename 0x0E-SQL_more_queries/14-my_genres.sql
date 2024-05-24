-- This query lists all genres of the show "Dexter" from the hbtn_0d_tvshows database.
-- It joins the tv_genres, tv_show_genres, and tv_shows tables to find the genres associated with "Dexter".
-- The results are sorted in ascending order by the genre name.

SELECT 
    tv_genres.name AS name  -- Select the genre name from the tv_genres table
FROM 
    tv_genres  -- Start with the tv_genres table
INNER JOIN 
    tv_show_genres  -- Join with the tv_show_genres table to link genres to shows
    ON tv_genres.id = tv_show_genres.genre_id  -- Match genres with their IDs in tv_show_genres
INNER JOIN 
    tv_shows  -- Join with the tv_shows table to link show IDs
    ON tv_show_genres.show_id = tv_shows.id  -- Match shows with their IDs in tv_show_genres
WHERE 
    tv_shows.title = 'Dexter'  -- Filter to select only the show "Dexter"
ORDER BY 
    tv_genres.name ASC;  -- Sort the results in ascending order by genre name


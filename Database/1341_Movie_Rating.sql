(
    select u.name as results
    from MovieRating as m join  Users as u on m.user_id = u.user_id 
    group by m.user_id
    order by count(*) desc, u.name 
    limit 1)


union 

(
    select m2.title as results
    from MovieRating as m1 join Movies as m2 on m1.movie_id = m2.movie_id
    where date_format(m1.created_at, "%Y-%m") = "2020-02"
    group by m1.movie_id
    order by avg(m1.rating) desc, m2.title
    limit 1);

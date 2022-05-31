{{ config(materialized='table') }}

with ranked_publiceations as (
    select
        title.preferred as article_title,
        doi,
        category.name as FOR_category,
        rank() over (partition by category.name order by metrics.times_cited desc) as top_cited,
        metrics.times_cited as citation_count
    from   
        `covid-19-dimensions-ai.data.publications`, 
        unnest ( category_for.first_level.full ) as category
)

select * from ranked_publiceations
where top_cited <= 3
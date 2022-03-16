{{ config(materialized='table') }}

SELECT *
FROM
    (
        SELECT
            title.preferred as article_title,
            doi,
            category.name as FOR_category,
            RANK() OVER (PARTITION BY category.name ORDER BY metrics.times_cited DESC) as top_cited,
            metrics.times_cited as citation_count
        FROM   
            `covid-19-dimensions-ai.data.publications`, 
            UNNEST ( category_for.first_level.FULL ) as category
    ) AS table_1
WHERE (top_cited <= 3)
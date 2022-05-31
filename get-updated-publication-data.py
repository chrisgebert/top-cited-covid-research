#######################################################################
#!/usr/bin/env python3
#######################################################################

# %% required libraries
import pandas as pd
from google.cloud import bigquery
import google.auth
import datetime


# %% BigQuery SQL query
query = """
with ranked_publications as (
    select
        title.preferred as article_title,
        doi,
        category.name as for_category,
        rank() over (partition by category.name order by metrics.times_cited desc) as top_cited,
        metrics.times_cited as citation_count
    from
        `covid-19-dimensions-ai.data.publications`,
        unnest ( category_for.first_level.full ) as category
)

select * from ranked_publications
where top_cited <=3
"""

# %% function 
def load_historical_data():
    df = pd.read_csv('data/COVID_publication_data.csv')
    return df

# %%
def get_latest_data():
    client = bigquery.Client()
    results = client.query(query)
    df = results.to_dataframe()
    df.loc[:, 'Date'] = str(datetime.date.today() - datetime.timedelta(days = 1))
    df.columns = ['Article Title', 'DOI', 'FOR Category', 'Top Cited Rank', 'Citation Count', 'Date']
    return df

# %%
historical_data = load_historical_data()
latest_publication_data = get_latest_data()
concat_df = pd.concat([latest_publication_data, historical_data], ignore_index=True)
concat_df.to_csv('data/COVID_publication_data.csv', index=False)

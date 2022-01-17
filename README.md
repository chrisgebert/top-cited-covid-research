# top-cited-covid-research

## Background

[Dimensions dataset of COVID-19 publications on BigQuery](https://console.cloud.google.com/marketplace/product/digitalscience-public/covid-19-dataset-dimensions)

Dimensions uses top-level FoR codes from the [Australian and New Zealand Standard Research Classification (ANZSRC)](https://www.abs.gov.au/statistics/classifications/australian-and-new-zealand-standard-research-classification-anzsrc/latest-release) to classify research publications in order to normalize comparative metrics for those publications. 

## Objective

This repository will periodically query the most recent version of the source dataset to create and append the 3 most top-cited research publications by FoR code to the existing results to track how those top positions change over time.

## Data File Schema

Fields in the [data file](/data/COVID_publication_data.csv) from the [Dimensions Publications Schema](https://docs.dimensions.ai/bigquery/datasource-publications.html):

| Field name | Description |
| ----------- | ----------- |
| `Article Title` | Title of publication, (`title`) |
| `DOI` | DOI of article, (`doi`) |
| `FOR Category` | Fields of Research classification, (`category_for`) |
| `Top Cited Rank` | Rank of paper (1, 2, or 3) |
| `Citation Count` | Number of citations, (`citations_count`) |
| `Date` | Date of snapshot |

Note: it's possible for the categorization to change as the machine learning model

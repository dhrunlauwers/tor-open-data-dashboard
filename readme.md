# Intro

This repo includes all code used and tableau files used to produce a set of dashboards showing the impact of COVID-19 on the Toronto real estate market, specifically, through the lens of development applications and building permits processed by the City of Toronto.

## Data sources 

Multiple datasets were gathered from the Toronto Open Data Catalogue:
- [Development Applications](https://open.toronto.ca/dataset/development-applications/)
- [Building Permits - Cleared Permits Prior Years](https://open.toronto.ca/dataset/building-permits-cleared-permits-prior-years/)
- [Building Permits - Cleared Permits Current Year](https://open.toronto.ca/dataset/building-permits-cleared-permits-current-year/)

In addition to this, some data was also gathered from Wikipedia to add context, specifically, the names of neighbourhoods that correspond to postal codes found in the data:
- [List of postal codes of Canada: M](https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M)

## Data pre-processing

Data was pre-processed in Python to facilitate dashboarding in Tableau:
- Building permits data was scattered accross different files for each year, so it was combined into one file and the date assigned based on the file name.
- The resulting dataset was quite large, so it was aggregated by year and postal code to support the multi-year dashboard.
- Dates had different formats accross different files, so some work was done to make them consistent before adding the data to Tableau.
- The first three letters of the postal code was used to tie together the data from the various files, which is then combined with the neighbourhood names from Wikipedia.
- Please see the [code](./code/) in this repository for more details.

## Dashboard

Two dashboards were built in order to help city officials assess the COVID-19 impact. 

First, a multi-year dashboard was constructed to show the overall trend in the number of business permits and development applications being processed. The information is broken down by neighbourhood and shows the primary use of building permits as well as the number of residential units created, lost, and the overall gain or loss in units. Users can move through time and see how each neighbourhood as doing before COVID kicked in during early 2020.

The second dashboard shows the more recent data along with year-over-year comparisons to allow users to more closely assess the impact of COVID-19. To assist users with their analysis and capture trends, a three month moving average was added in addition to the actual data to smooth out the impact of month-over-month volatility. Common filters as well as filters specific to both building permits and development applications were added to allow users to drill down on the data as necessary. 

Note that building permits without dates associated with them were removed for this analysis, which may result in some discrepancies between the totals of the multi-year dashboard where file name was used to denote the period.
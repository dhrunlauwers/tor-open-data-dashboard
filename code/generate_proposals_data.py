import pandas as pd

# development applications
apps_df_raw = pd.read_csv('../data/development-applications/Development Applications Data.csv')

# copy original data to compare later
apps_df = apps_df_raw.copy()

# change date cols to datetime
apps_df['DATE_SUBMITTED'] = pd.to_datetime(apps_df['DATE_SUBMITTED'])

# filter out old data and 2021 data
apps_df = apps_df[apps_df['DATE_SUBMITTED'] >= pd.to_datetime('01-01-2012')]
apps_df = apps_df[apps_df['DATE_SUBMITTED'] <= pd.to_datetime('12-31-2020')]

# remove rows that are missing postal code
apps_df = apps_df[apps_df['POSTAL'] != '   ']

# create year column for grouping
apps_df['Year'] = apps_df['DATE_SUBMITTED'].dt.year

# create column of 1s for counting
apps_df['Development Application Count'] = 1

# group data
grouped_apps = apps_df.groupby(['Year', 'POSTAL', 'APPLICATION_TYPE']).agg('sum').reset_index()

# write out to file
grouped_apps.to_csv('../data/processed/grouped_applications.csv', index=False)
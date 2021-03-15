import pandas as pd

# development applications
apps_df_raw = pd.read_csv('../data/development-applications/Development Applications Data.csv')

# copy original data to compare later
apps_df = apps_df_raw.copy()

# change date cols to datetime
apps_df['DATE_SUBMITTED'] = pd.to_datetime(apps_df['DATE_SUBMITTED'])

# filter out old data after 2019
apps_df = apps_df[apps_df['DATE_SUBMITTED'] >= pd.to_datetime('01-01-2019')]

# remove rows that are missing postal code
apps_df = apps_df[apps_df['POSTAL'] != '   ']

# write out to file
apps_df.to_csv('../data/processed/applications2019to2021.csv', index=False)
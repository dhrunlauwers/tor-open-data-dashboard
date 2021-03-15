import glob
import pandas as pd

# grab all data and concat into a single dataframe
perms_path = '../data/building-permits/'
all_files = glob.glob(perms_path+"/*.csv")

df_list = []

for file_name in all_files:
    df = pd.read_csv(file_name, index_col=None, header=0)
    df['year_from_file_name'] = file_name[-8:-4]
    df_list.append(df)

perms_df_raw = pd.concat(df_list, axis=0, ignore_index=True)

#make a copy to compare after processing
perms_df = perms_df_raw.copy()

# change date cols to datetime
perms_df['APPLICATION_DATE'] = pd.to_datetime(perms_df['APPLICATION_DATE'])

# create columns of 1s for counting
perms_df['Building Permit Count'] = 1

# remove rows that are missing postal code
perms_df = perms_df[perms_df['POSTAL'] != '   ']

# group data by year, postal and permit type
grouped_perms = perms_df.groupby(['year_from_file_name', 'POSTAL']).agg('sum')

# normalize land area data for easier use in tableau
norm_cols = ['ASSEMBLY', 'INSTITUTIONAL', 'RESIDENTIAL', 'BUSINESS_AND_PERSONAL_SERVICES','MERCANTILE','INDUSTRIAL','DEMOLITION','INTERIOR_ALTERATIONS']
land_area_df = pd.DataFrame(grouped_perms[norm_cols].stack()).reset_index()
land_area_df.rename(columns={'level_2':'Land Area Type', 0:'Land Area Affected'}, inplace=True)

# drop unnecessary columns
norm_cols.append('GEO_ID')
grouped_perms.drop(norm_cols, axis='columns', inplace=True)

# create net dwellings column
grouped_perms['Dwelling Units Net'] = grouped_perms['DWELLING_UNITS_CREATED'] - grouped_perms['DWELLING_UNITS_LOST']

# write results to file
land_area_df.to_csv('../data/processed/permits_land_area.csv', index=False)
grouped_perms.reset_index().to_csv('../data/processed/permits_issued.csv', index=False)

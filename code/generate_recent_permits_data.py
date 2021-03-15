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

# filter on just the most recent years
recent_years = ['2019','2020', '2021']
perms_df['app_date_year'] = perms_df['APPLICATION_DATE'].apply(lambda x: str(x)[:4])
recent_perms_df = perms_df[perms_df['app_date_year'].isin(recent_years)]

# fix date column
def fix_date(bad_date):
    
    if len(str(bad_date)) > 10:
        result = pd.to_datetime(str(bad_date)[:8])
    else:
        result = pd.to_datetime(str(bad_date))
        
    return result

recent_perms_df['APPLICATION_DATE'] = recent_perms_df['APPLICATION_DATE'].apply(lambda x: fix_date(x))

# write result to file
recent_perms_df.to_csv('../data/processed/permits2019to2021.csv')
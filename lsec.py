import pandas as pd
from IPython.display import display
# converting list into dataframe
# calculating total seconds

# ini list
l1 = [('00:0:25', '00:01:2'), ('0:2:38', '00:03:07'), ('00:04:17', '00:4:31'), ('1:4:40', '01:04:48')]
# print(l1)
# converting to dataframe
df = pd.DataFrame(l1, columns = ['start', 'end'])
# print(df)

# convert datetime to timedelta
df['start'] = pd.to_timedelta(df['start'])
# calculate total seconds and change to integer type
df['start'] = df['start'].dt.total_seconds().astype(int)
# print(df)
# df.info(verbose=True)




# df[["String 1", "String 2"]] = df[["String 1", "String 2"]].apply(prepend_geek)

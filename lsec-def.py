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

# custom function to convert string to total_seconds
def str_to_sec(colname):
    colname = pd.to_timedelta(colname)
    return colname.dt.total_seconds().astype(int)

# applying custom function to all columns
df[['start', 'end']] = df[['start', 'end']].apply(str_to_sec)
print(df)
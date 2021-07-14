import re
from datetime import datetime, timedelta
import pandas as pd

# duration = end - start
# offset = running total of duration

#ini list
ls1 = [1,2,3]
ls2 = [4,6,8]

#ini tuple
tplx = [(1, 2, 3), (4, 6, 8)]

# ini tuple
tpl1 = (1, 2, 3)
tpl2 = (4, 6, 8)

#ini df
dict={'start':[1, 2, 3],'end':[4, 6, 8]}
df = pd.DataFrame(dict)

# substraction with tuple
tpl3 = tuple(map(lambda i, j: j - i, tpl1, tpl2))
# print(tpl3)
# print(type(tpl3))

# substraction with list
ls3 = []
for i in range(len(ls1)):
    ls3.append(ls2[i] - ls1[i])
# print(ls3)

# substraction with df
df['duration'] = df.end - df.start
# print(df)
#calculating offset column
df['offset']=df.duration.cumsum()
# print(df)
# shifting offset
df.offset = df.offset.shift(+1)
# print(df)
# assigning first row to 0
df.offset[0] = 0
# print(df)
# changing type to ineger
df.offset = df.offset.astype(int)
# print(df)
# selecting columns
print(df[['start', 'duration', 'offset']])


# ini lists
ls5 = ['a', 'b', 'g', 'w']
ls6 = ['d', 'a', 'r', 'l']

# creating dataframe from lists
lsz = list(zip(ls5,ls6))
# print(lsz)
df1 = pd.DataFrame(lsz, columns = ['name1', 'name2'])
# print(df1)

# converting dataframe to list
df2 = df1.values.tolist()
# print(df2)
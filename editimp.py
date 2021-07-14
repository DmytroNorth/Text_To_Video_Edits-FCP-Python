#!/usr/bin/env python

import re
import pandas as pd

# intializing .txt file with a list of markers
edt = open('assets/edl.txt').read()

# intializing .fcpxml file with at least 1 marker
fcp = open('assets/clip.fcpxml').read()

#STRING REGEX OPERATIONS
# puting '00:' hours in where hours are missing
pat1 = r'(\s|^)(\d{1,2}:\d{1,2})(\s)'
repl1 = '\g<1>00:\\2\\3'
edt1 = re.sub(pat1, repl1, edt, flags=re.MULTILINE)
# print(edt1)

# pulling instanses with two timecodes in one line only
pat2 = r'.*?(\d{1,2}:\d{1,2}:\d{1,2}).*?(\d{1,2}:\d{1,2}:\d{1,2})'
edt2 = re.findall(pat2, edt1)
# print(edt2)

#DATAFRAME CONVERSION
# converting to dataframe
df = pd.DataFrame(edt2, columns = ['start', 'end'])
# print(df)

# building custom function to convert string to total seconds
def str_to_sec(colname):
    colname = pd.to_timedelta(colname)
    return colname.dt.total_seconds().astype(int)

# applying custom function to all columns
df[['start', 'end']] = df[['start', 'end']].apply(str_to_sec)
# print(df)

#DATAFRAME OPERATIONS
# substraction with df
df['duration'] = df['end'] - df['start']
#calculating offset column and shifting one row below
df['offset']=df['duration'].cumsum().shift(+1)
# filling NA values with 0 and assigning type integer
df = df.fillna(0).astype(int)
# print(df)

#STRING ASSEMBLY
# pulling chunks of strings form fcpxml to assemble <ref-clip> tag
pat6 = r'(.*?<ref-clip.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
fcp2 = re.findall(pat6, fcp)

# combining created lists
lcomb = []
for i in range(len(df)):
    lcomb.append(fcp2[0][0] + str(df.offset[i]) + fcp2[0][1] + str(df.duration[i])+fcp2[0][2] + str(df.start[i])+ fcp2[0][3])
# print(lcomb)

# converting list into a string
sub = '\n'.join(lcomb)
# print(sub)

#XML ASSEMBLY
# replacing ref-clip markers with newly assembled
pat8 = r'( +<ref-clip.*?\n)+'
repl8 = sub + '\n'
fcp6 = re.sub(pat8, repl8, fcp)
# print(fcp6)

# writing to a new .fcpxml file
with open('export.fcpxml', 'w') as newfile:
    newfile.write(fcp6)
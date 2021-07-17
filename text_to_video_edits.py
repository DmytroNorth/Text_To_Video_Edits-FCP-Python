#!/usr/bin/env python3

import re
import pandas as pd

# intializing .txt file with a list of markers
edt = open('videoedits.txt').read()

# intializing .fcpxml file with at least 1 marker
fcp = open('clip.fcpxml').read()
# print('\n'.join(re.findall(r'.*?<ref-clip.*?>', fcp)))


# STRING REGEX OPERATIONS
# puting '00:' hours in where hours are missing
pat1 = r'(\s|^)(\d{1,2}:\d{1,2})(\s|$)'
repl1 = "\g<1>00:\\2\\3"
edt1 = re.sub(pat1, repl1, edt, 0, re.MULTILINE)
print(edt1)

# pulling instanses with two timecodes in one line
pat2 = r'.*?(\d{1,2}:\d{1,2}:\d{1,2}).*?(\d{1,2}:\d{1,2}:\d{1,2})'
edt2 = re.findall(pat2, edt1)
# print(edt2)

# DATAFRAME CONVERSION
# converting to dataframe
df = pd.DataFrame(edt2, columns=['start', 'end'])
# print(df)

# building custom function to convert string to total seconds


def str_to_sec(colname):
    colname = pd.to_timedelta(colname)
    return colname.dt.total_seconds().astype(int)


# applying custom function to all columns
df[['start', 'end']] = df[['start', 'end']].apply(str_to_sec)
# print(df)

# DATAFRAME OPERATIONS
# edt3straction with df
df['duration'] = df['end'] - df['start']
# calculating offset column and shifting one row below
df['offset'] = df['duration'].cumsum().shift(+1)
# filling NA values with 0 and assigning type integer
df = df.fillna(0).astype(int)
# print(df)44

# STRING ASSEMBLY
# pulling chunks of strings form fcpxml to assemble <ref-clip> tag
pat3 = r'(.*?<ref-clip.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
fcp1 = re.findall(pat3, fcp)
# print(fcp1)

# combining created lists
lcomb = []
for i in range(len(df)):
    lcomb.append(fcp1[0][0] + str(df.offset[i]) + fcp1[0][1] +
                 str(df.duration[i])+fcp1[0][2] + str(df.start[i]) + fcp1[0][3])
# print(lcomb)

# converting list into a string
edt3 = '\n'.join(lcomb)
# print(edt3)

# XML ASSEMBLY
# replacing ref-clip markers with newly assembled
pat4 = r'( +<ref-clip.*?\n)+'
repl4 = edt3 + '\n'
fcp2 = re.sub(pat4, repl4, fcp)
# print(fcp2)

# writing to a new .fcpxml file
with open('export.fcpxml', 'w') as newfile:
    newfile.write(fcp2)
# print('\n'.join(re.findall(r'.*?<ref-clip.*?>', fcp2)))

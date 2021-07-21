#!/usr/bin/env python3
import os
import re
import pandas as pd

# intializing .txt file with a list of edits
inputtxt = 'videoedits.txt'
txtpath = os.path.join(os.path.dirname(__file__), inputtxt)
edt = open(txtpath).read()

# intializing .fcpxml file with at least 1 marker
inputxml = 'clip.fcpxml'
xmlpath = os.path.join(os.path.dirname(__file__), inputxml)
fcp = open(xmlpath).read()


# STRING REGEX OPERATIONS
# puting '00:' hours in where hours are missing
pat1 = r'(\s|^)(\d{1,2}:\d{1,2})(\s|$)'
repl1 = "\g<1>00:\\2\\3"
edt1 = re.sub(pat1, repl1, edt, 0, re.MULTILINE)

# pulling instanses with two timecodes in one line
pat2 = r'.*?(\d{1,2}:\d{1,2}:\d{1,2}).*?(\d{1,2}:\d{1,2}:\d{1,2})'
edt2 = re.findall(pat2, edt1)

# DATAFRAME CONVERSION
# converting to dataframe
df = pd.DataFrame(edt2, columns=['start', 'end'])

# building custom function to convert string to total seconds


def str_to_sec(colname):
    colname = pd.to_timedelta(colname)
    return colname.dt.total_seconds().astype(int)


# applying custom function to all columns
df[['start', 'end']] = df[['start', 'end']].apply(str_to_sec)

# DATAFRAME OPERATIONS
# edt3straction with df
df['duration'] = df['end'] - df['start']
# calculating offset column and shifting one row below
df['offset'] = df['duration'].cumsum().shift(+1)
# filling NA values with 0 and assigning type integer
df = df.fillna(0).astype(int)

# STRING ASSEMBLY
# pulling chunks of strings form fcpxml to assemble <ref-clip> tag
pat3 = r'(.*?<ref-clip.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
fcp1 = re.findall(pat3, fcp)

# combining created lists
lcomb = []
for i in range(len(df)):
    lcomb.append(fcp1[0][0] + str(df.offset[i]) + fcp1[0][1] +
                 str(df.duration[i])+fcp1[0][2] + str(df.start[i]) + fcp1[0][3])


# converting list into a string
edt3 = '\n'.join(lcomb)

# XML ASSEMBLY
# replacing ref-clip markers with newly assembled
pat4 = r'( +<ref-clip.*?\n)+'
repl4 = edt3 + '\n'
fcp2 = re.sub(pat4, repl4, fcp)

# writing to a new .fcpxml file
xml2 = os.path.join(os.path.dirname(__file__), 'export.fcpxml')
with open(xml2, 'w') as newfile:
    newfile.write(fcp2)

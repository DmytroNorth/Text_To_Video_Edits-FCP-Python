#!/usr/bin/env python

import re
from datetime import datetime, timedelta

# initialize str
edt3 = '00:0:25 00:01:2 00:2:38 00:03:08 00:04:18 00:4:31 1:4:40 01:04:48'
# define the regex pattern

pat1 = r'(\d{1,2}:\d{1,2}:\d{1,2})'
# initiallize replace function

def repl1(tc):
    # convert re.Match class to string
    tc1 = tc.group()
    # convert string to datetime
    dt = datetime.strptime(tc1, '%H:%M:%S')
    # convert datetime to timedelta
    td = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
    # calculate total seconds
    tsec = td.seconds
    # convert total seconds to string
    return str(tsec)

#perform regex substitution
find1 = re.sub(pat1, repl1, edt3)
print(find1)
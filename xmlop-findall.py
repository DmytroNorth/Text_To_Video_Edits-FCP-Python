#!/usr/bin/env python

import re
# from datetime import datetime, timedelta
import pandas as pd

# intializing .txt file with a list of markers
edt = open('assets/edl.txt').read()

# intializing .fcpxml file with at least 1 marker
fcp = open('assets/clip.fcpxml').read()

# assigning varibles to <marker> parts of syntax
pat6 = r'(.*?<ref-clip.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
fcp2 = re.findall(pat6, fcp)
# print(fcp2[0][0])
# print(fcp2[0][1])
# print(fcp2[0][2])
# print(fcp2[0][3])
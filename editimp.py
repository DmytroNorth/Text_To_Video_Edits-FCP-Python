#!/usr/bin/env python

import re
from datetime import datetime, timedelta

# intializing .txt file with a list of markers
edt = open('assets/edl.txt')
edt = edt.read()

# intializing .fcpxml file with at least 1 marker
fcp = open('assets/clip.fcpxml')
fcp = fcp.read()

# puting '00:' hours in where hours are missing
pat3 = r'(\s|^)(\d{1,2}:\d{1,2})(\s)'
repl3 = '\g<1>00:\\2\\3'
edt3 = re.sub(pat3, repl3, edt, flags=re.MULTILINE)
# print(edt3)

pat4 = r'.*?(\d{1,2}:\d{1,2}:\d{1,2}).*?(\d{1,2}:\d{1,2}:\d{1,2})'
edt4 = re.findall(pat4, edt3)
# print(edt4)


# # converting %H:%M:%S to total seconds
# pat4 = r'(\d{1,2}:\d{1,2}:\d{1,2})'
# def repl4_converted_to_seconds(timestamp):
#     timestamp = timestamp.group()
#     dt = datetime.strptime(timestamp, '%H:%M:%S')
#     delta = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
#     return str(delta.seconds)
# edt4 = re.sub(pat4, repl4_converted_to_seconds, edt3)
# print(edt4)

# # converting %H:%M:%S to total seconds
# pat4 = r'(\d{1,2}:\d{1,2}:\d{1,2})'
# def repl4_converted_to_seconds(timestamp):
#     timestamp = timestamp.group()
#     dt = datetime.strptime(timestamp, '%H:%M:%S')
#     delta = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
#     return '$' + str(delta.seconds) + '@'
# edt4 = re.sub(pat4, repl4_converted_to_seconds, edt3)
# print(edt4)

# pulling first instance of <ref-clip> line from fcpxml
pat5 = r'.*?<ref-clip.*?>'
fcp1 = re.search(pat5, fcp)
fcp1 = fcp1.group()
print(fcp1)

# assigning varibles to <marker> parts of syntax
pat6 = r'(.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
repl5 = '\\1'
repl6 = '\\2'
repl7 = '\\3'
repl7a = '\\4'
fcp2 = re.sub(pat6, repl5, fcp1)
fcp3 = re.sub(pat6, repl6, fcp1)
fcp4 = re.sub(pat6, repl7, fcp1)
fcp4a = re.sub(pat6, repl7a, fcp1)
# print(fcp2)
# print(fcp3)
# print(fcp4)
# print(fcp4a)

# # assemblying new marker lines
# pat7 = r'(^\d*) (.*)'
# repl8 = fcp2 + '\\1' + fcp3 + '\\2' + fcp4 + '\\3' + fcp4a
# fcp5 = re.sub(pat7, repl8, edt4, flags=re.MULTILINE)

# # assemblying fcpxml code
# pat8 = r'(^\s*<marker.*$)'
# repl8 = fcp5 + '\n\\1'
# fcp6 = re.sub(pat8, repl8, fcp, 1, flags=re.MULTILINE)

# # writing to a new .fcpxml file
# with open('export.fcpxml', 'w') as newfile:
#     newfile.write(fcp6)
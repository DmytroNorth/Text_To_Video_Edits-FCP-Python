import pandas as pd

# xml operations

# ini string
ref = '<ref-clip name="ocean_clip" offset="0s" ref="r2" duration="37s" start="25s"/>'

# ini df
df={'start':[1, 2, 3],'duration':[4, 6, 8], 'offset':[7, 8, 9]}
df = pd.DataFrame(df)

# pulling list
l1 = (list(df.start))

# ini strings
str1 = 'xxx'
str2 = 'yyy'

# combining created lists
lcomb = []
for i in range(len(df.start)):
    lcomb.append(str1 +  str(df.start[i]) + str2)
# print(lcomb)

# converting list into a string
sub = '\n'.join(lcomb)
print(sub)




# # pulling first instance of <ref-clip> line from fcpxml
# pat5 = r'.*?<ref-clip.*?>'
# fcp1 = re.search(pat5, fcp)
# fcp1 = fcp1.group()
# # print(fcp1)

# # assigning varibles to <marker> parts of syntax
# pat6 = r'(.*?offset=").*?(".*duration=").*?(".*start=").*?(".*)'
# repl5 = '\\1'
# repl6 = '\\2'
# repl7 = '\\3'
# repl7a = '\\4'
# fcp2 = re.sub(pat6, repl5, fcp1)
# fcp3 = re.sub(pat6, repl6, fcp1)
# fcp4 = re.sub(pat6, repl7, fcp1)
# fcp4a = re.sub(pat6, repl7a, fcp1)
# # print(fcp2)
# # print(fcp3)
# # print(fcp4)
# # print(fcp4a)

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
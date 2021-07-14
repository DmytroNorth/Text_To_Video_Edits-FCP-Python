#!/usr/bin/env python

import re
import pandas as pd

str1 = '''       <sequence duration="16200/3000s" format="r1" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
                    <spine>
                        <ref-clip name="ocean_clip" offset="0s" ref="r2" duration="8000/3000s" start="15800/3000s"/>
                        <ref-clip name="ocean_clip" offset="8000/3000s" ref="r2" duration="8200/3000s" start="5900/3000s"/>
                        <ref-clip name="ocean_clip" offset="0s" ref="r2" duration="8000/3000s" start="20800/3000s"/>
                    </spine>
                </sequence>'''

str2 = '''                        <ref-clip name="ocean_clip" offset="0" ref="r2" duration="37" start="25"/>
                        <ref-clip name="ocean_clip" offset="37" ref="r2" duration="29" start="158"/>
                        <ref-clip name="ocean_clip" offset="66" ref="r2" duration="14" start="257"/>
                        <ref-clip name="ocean_clip" offset="80" ref="r2" duration="8" start="3880"/>'''

#XML ASSEMBLY
# replacing ref-clip with a placeholder
pat8 = r'( +<ref-clip.*?\n)+'
repl8 = str2 + '\n'
fcp6 = re.sub(pat8, repl8, str1, flags=re.MULTILINE)
print(fcp6)



# # replacing ref-clip with a placeholder
# pat8 = r'(^\s*<ref-clip.*\n)'
# repl8 = '%&@'
# fcp6 = re.sub(pat8, repl8, str1, flags=re.MULTILINE)
# # print(fcp6)

# # replacing placeholder with ref-clip strings
# pat9 = r'(%&@)+'
# repl9 = str2
# fcp7 = re.sub(pat9, repl9, fcp6, flags=re.MULTILINE)
# print(fcp7)
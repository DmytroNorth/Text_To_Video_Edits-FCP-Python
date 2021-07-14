#!/usr/bin/env python

import re
import pandas as pd

# ini string
ref = '<ref-clip name="ocean_clip" offset="0s" ref="r2" duration="37s" start="25s"/>'

# ini df
df={'start':[1, 2, 3],'duration':[4, 6, 8], 'offset':[7, 8, 9]}
df = pd.DataFrame(df)

l1 = (list(df.start))

for i in list(df.start):
    list.append('xx %d yy' % i)
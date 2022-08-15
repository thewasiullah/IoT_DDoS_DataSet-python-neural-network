import os
from pathlib import Path
import sys
import pandas as pd

# cwd = Path.cwd()

# print(cwd)
# dir_name = "D:\\SemesterSummer\\ML\\RP\\Urban_IoT_DDoS_Data-main\\source_code\\test\\deleteThis"
# os.removedirs(dir_name)
# os.mkdir(dir_name)
print(sys.path)
dfx = pd.Series(['30-01-2016', '15-09-2015', '40-09-2016', '2021-01-31 08:10:30'])
print (dfx)

dfx = pd.to_datetime('2021-01-31 08:10:30')
print (dfx)

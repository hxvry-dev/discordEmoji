import csv
import datetime as dt
import colorama
import textwrap

ts = dt.datetime.now()
date = ts.strftime("%m%d%Y")
time = ts.strftime("%H%M%S")
print(date + " " + time)

# Using writelines to programatically generate outputs
from datetime import *
import pandas as pd
import pprint
import re

nitroStatus = input("Nitro Status [Y/n] >> ")
inline_stats = input("Inline Stats [Y/n] >> ")
ns = re.sub("[eso]", "", nitroStatus).lower().strip()
en = input("Emoji >> ")
inline = re.sub("[eso]", "", inline_stats).lower().strip()

en_lower = en.lower()
en_formatted = ":" + en_lower + ":"
en_length = len(en_formatted)

clock = datetime.now()
date = clock.strftime("%Y%m%d")
time = clock.strftime("%H%M%S")
dt = clock.strftime("%Y%m%d%H%M")
pp = pprint.PrettyPrinter()

df = pd.DataFrame()

ts = date + "_" + en_lower + "_" + time

f = open("./emoji/" + dt + "-" + en_lower + "-beta.json", "w", newline="")

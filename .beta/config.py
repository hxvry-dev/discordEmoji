from datetime import *
import re

nitroStatus = input('Nitro Status [Y/n] >> ')
ns = re.sub('[eso]', '', nitroStatus).lower().strip()
en = input('Emoji >> ')

en_lower = en.lower()
en_formatted = ":" + en_lower + ":"
en_length = len(en_formatted)

clock = datetime.now()
date = clock.strftime('%Y%m%d')
time = clock.strftime('%H%M%S')


ts = date + "_" + en_lower + "_" + time
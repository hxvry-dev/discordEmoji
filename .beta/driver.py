# Beta release v1.0.2

import pprint
import json
import config as c
from datetime import *

emoji = {}
stats = []
dump = json.dumps(emoji, indent=4, )

class Emoji:
    # Welcome to the EmojiMaker v2.0!
    # To start, please supply the following configuration data:
        # - The Discord emoji you want to create (For example :fire:)
        # - Whether or not you have Discord Nitro (To determine how long to make the message)
        # TODO: Create the ability to specify how many emoji are in each row
        # TODO: FINISH this!
    
    def __init__(self):
        self.e = emoji
        self.s = stats
        self.en = c.en
        self.en_lower = c.en_lower
        self.en_formatted = c.en_formatted
        self.en_length = c.en_length
        self.ns = c.ns
        self.ts = c.ts
        self.date = c.date
        self.time = c.time
    
    def gainIntel(self, *args):
        for arg in args:
            stats.append(arg)
        emoji['Emoji'] = stats[1]
        emoji['Nitro Status'] = stats[0]
        emoji['Stats'] = {
            "Timestamp": stats[2],
            "Time": stats[4],
            "Date": stats[3],
            "Length of the Formatted Emoji": stats[7]
            }
        emoji['Formatted Emoji'] = [stats[5]]
        emoji['Final Stats'] = {
            "Stats": stats
        }
        print(json.dumps(emoji, indent=4))
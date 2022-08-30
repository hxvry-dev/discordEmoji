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
        self.ns = c.ns
        self.ts = c.ts
    
    def makeEmoji(self, en, ns, ts):
        stats.append(en)
        stats.append(ns)
        stats.append(ts)
        
        print(stats)
        emoji['Emoji'] = stats[1]
        emoji['Nitro Status'] = stats[0]
        print(json.dumps(emoji, indent=4))
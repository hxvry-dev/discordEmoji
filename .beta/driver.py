# Beta release v1.0.2

import pprint
import json
import config as c
from colorama import *
from datetime import *
init()

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
        self.ts = c.ts
        self.en = c.en
        self.ns = c.ns
    
    def makeEmoji(self, en, ns, ts):
        stats.extend((ts, en, ns))
        emoji['Emoji'] = stats[2]
        emoji['Nitro Status'] = stats[1]
        print(stats)
        print(json.dumps(emoji, indent=4))
# Beta release v1.0.2

import pprint
import json
from . import config
from colorama import *
from datetime import *
init()

class Emoji:
    blurb = """
    Welcome to the EmojiMaker v2.0!
    To start, please supply the following configuration data:
        - The Discord emoji you want to create (For example :fire:)
        - Whether or not you have Discord Nitro (To determine how long to make the message)
    """
    
    # TODO: Create the ability to specify how many emoji are in each row
    
    def __init__(self):
        self.ts = config.ts
        self.en = config.en
        self.ns = config.ns
        self.emoji = {}
        self.stats = []
    
    def makeEmoji(self, en, ns, ts):
        self.emoji.append("[ " + ts + " ]" + "The Raw Text for the Emoji: " + en)
        self.emoji.append("Nitro Status: " + ns)
        print(self.emoji)
        return en, ns, ts
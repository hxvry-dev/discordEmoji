# Beta release v1.0.2

import pandas as pd
import json
import csv
import config as c
from datetime import *


class Emoji:
    # Welcome to the EmojiMaker v2.0!
    # To start, please supply the following configuration data:
    # - The Discord emoji you want to create (For example :fire:)
    # - Whether or not you have Discord Nitro (To determine how long to make the message)
    # TODO: Create the ability to specify how many emoji are in each row
    # TODO: FINISH this!

    def gainIntel(self, *args):
        i = 0
        for arg in args:
            self.stats[i] = arg
            i += 1
        self.emoji["Stats"] = {
            "Emoji": self.stats[2],
            "Nitro Status": self.stats[1],
            "Time": self.stats[5],
            "Date": self.stats[4],
            "Timestamp": self.stats[3],
            "Formatted Emoji": self.stats[6],
            "Length of the Formatted Emoji": self.stats[8],
        }
        self.emoji["Final Stats"] = self.stats
        print(self.emoji)
        print(self.stats)

    def makeEmoji(self, *args):
        for arg in args:
            self.emojiList.append(arg)

    def __init__(self):
        self.pp = c.pp
        # self.f = c.f
        self.df = c.df
        self.emojiList = []
        self.stats = {}
        self.emoji = {}
        self.dump = json.dumps(self.emoji, indent=4)
        self.en = c.en
        self.en_lower = c.en_lower
        self.en_formatted = c.en_formatted
        self.en_length = c.en_length
        self.ns = c.ns
        self.ts = c.ts
        self.date = c.date
        self.time = c.time

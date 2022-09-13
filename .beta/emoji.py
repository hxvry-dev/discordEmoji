# Beta release v1.0.2
import pprint
import re
import json
import pandas as pd
from datetime import *


class Emoji:
    # Welcome to the EmojiMaker v2.0!
    # To start, please supply the following configuration data:
    # - The Discord emoji you want to create (For example :fire:)
    # - Whether or not you have Discord Nitro (To determine how long to make the message)
    # TODO: Create the ability to specify how many emoji are in each row
    # TODO: FINISH this!

    def gainIntel(self, *args):
        self.i = 0
        for arg in args:
            self.stats[self.i] = arg
            self.i += 1
        self.emoji = {
            "Emoji": self.stats[2],
            "Nitro Status": self.stats[1],
            "Time": self.stats[5],
            "Date": self.stats[4],
            "Timestamp": self.stats[3],
            "Formatted Emoji": self.stats[6],
            "Length of the Formatted Emoji": self.stats[8],
        }
        print(
            "\n\nEmoji Stats [Formatted]\n"
            + str(self.emoji)
            + "\n\nEmoji Stats [Unformatted]\n"
            + str(self.stats)
        )

    def makeEmoji(self, *args):
        for arg in args:
            self.emojiList.append(arg)

        self.df = pd.DataFrame(data=self.emoji, index=[0])

        print("\n\n{}".format(self.df) + "\nColumns:{}".format(self.df.columns))


e = Emoji()
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

ts = date + "_" + en_lower + "_" + time

e.gainIntel(
    inline,
    ns,
    en,
    ts,
    date,
    time,
    en_formatted,
    en_lower,
    en_length,
)

e.makeEmoji(en_length, en_formatted, en_lower)
"""
    "index": "value"
    "Final Stats": {
        "Stats": {
            "0": "y",
            "1": "y",
            "2": "yes",
            "3": "20220910_yes_222046",
            "4": "20220910",
            "5": "222046",
            "6": ":yes:",
            "7": "yes",
            "8": 5
        }
    }
"""


def __init__(self):
    pass

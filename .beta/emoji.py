import driver
import config as c

e = driver.Emoji()

e.gainIntel(c.inline, c.ns, c.en, c.ts, c.date, c.time,
            c.en_formatted, c.en_lower, c.en_length)

'''
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
'''

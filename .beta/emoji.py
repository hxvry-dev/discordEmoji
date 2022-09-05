import driver
import config as c

e = driver.Emoji()

#   0    1     2               3                4          5        6       7    8
#   |    |     |               |                |          |        |       |    |
# ['y', 'y', 'yes', '20220830_yes_214736', '20220830', '214736', ':yes:', 'yes', 5]
e.gainIntel(c.inline,c.ns,c.en,c.ts,c.date,c.time,c.en_formatted,c.en_lower,c.en_length)
#This is a test commit
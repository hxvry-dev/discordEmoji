import datetime as dt
from colorama import Fore
import re

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
    def __init__(self):
        self.lines = ''
        self.emoji = input(console + "Name of the Emoji as It appears in Discord >> ")

    def wFile(self):
        ts = dt.datetime.now()
        t = ts.strftime('%Y%m%d%H%M%S')
        date = ts.strftime("%m%d%Y")
        time = ts.strftime("%H%M%S")
        self.lines += "\tEmoji [Not Formatted] >> " + self.emoji
        with open('./emoji/' + t + "-" + self.emoji + '.txt', 'w') as f:
            f.write("Welcome to the EmojiMaker v2.0!\n\n")
            f.write(self.lines + '\n')

def main():
    e = Emoji()
    e.wFile()

if __name__ == '__main__':
    main()
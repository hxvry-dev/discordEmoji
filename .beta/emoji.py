import datetime as dt
from colorama import Fore
import re

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
    def __init__(self):
        self.lines = ''
        self.emoji = self.getEmoji()
    
    def getEmoji(self):
        return input(console + "Name of the Emoji as it appears in Discord >> ")

    def wFile(self):
        ts = dt.datetime.now()
        t = ts.strftime('%Y%m%d%H%M%S')
        date = ts.strftime("%m%d%Y")
        time = ts.strftime("%H%M%S")
        head = '''<!DOCTYPE html>
<html>
  <head>
    <title>Emoji Result</title>
  </head>
  <body>
  <h1 style="padding-left: 5px">Welcome to the EmojiMaker v2.0!</h1></br>
    <h1 style="padding-left: 15px">{Idea}</h1>
  </body>
</html>'''
        with open('./emoji/' + t + "-" + self.emoji + '.html', 'w') as f:
            f.write(head)

def main():
    e = Emoji()
    e.wFile()
if __name__ == '__main__':
    main()
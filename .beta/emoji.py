import datetime as dt
from colorama import Fore
from airium import Airium

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  a = Airium()
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

def main():
  e = Emoji()
  e.wFile()

if __name__ == '__main__':
    main()
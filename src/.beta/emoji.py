import datetime as dt
from colorama import Fore
from airium import Airium
import os

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  def __init__(self):
    print(os.getcwd())
    self.t = dt.datetime.now().strftime('%Y%m%d%H%M%S')
    #Commenting this out for easy running of the file
    #self.name = input(console + "Name of the Emoji as it appears in Discord >> ")

  def basic_body(self):          # '-' + self.name + 
    f = open('./emoji/v2/' + self.t + '--beta' + '-' +  dt.datetime.now().strftime('%M%S') + '.html', 'w')
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang='en'):
      with a.head():
        a.meta(charset='utf-8')
        a.link(href='../.beta/styles/content.css', rel='stylesheet')
        a.title(_t=f'Welcome to the emojiMaker v2.0!')
      with a.body():
        with a.div(klass='container'):
            a.p(id='item', _t='This is your emoji as it appears in the Discord Emoji Search bar >')
            a.code(_t=self.t)

    html = str(a)
    f.write(html)
    f.close()

def main():
  e = Emoji()
  e.basic_body()


if __name__ == '__main__':
    main()
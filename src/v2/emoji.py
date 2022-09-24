import random
import time
from colorama import Fore
from airium import Airium

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  def __init__(self):
    self.x = str(random.randint(1, 9999999))
    self.name = input(console + "Name of the Emoji as it appears in Discord >> ")
    self.nitro_status = input(console + "Do you have Discord Nitro? [y/n] >> ").lower().strip('eso')

  def basic_body(self):                            # + self.name + 
    f = open('./emoji/v2/' + self.x + '-beta-' + self.name + '.html', 'w')
    a = Airium()
    print(info + '--BEGINNING BASIC BODY CONSTRUCTION--')
    a('<!DOCTYPE html>')
    with a.html(lang='en'):
      with a.head():
        a.meta(charset='utf-8')
        a.link(href='../../src/v2/styles/content.css', rel='stylesheet')
        a.title(_t=f'Welcome to the emojiMaker v2.0!')
      with a.body():
        with a.div(klass='container'):
          a.p(id='item', _t='Random number so the file is unique >')
          a.code(_t=self.x)
          a.br()
          a.p(id='item', _t='If you have <code>Discord Nitro</code> or not >')
          a.code(_t=self.nitro_status)
          a.br()
          a.p(id='item', _t='Input formatted to look like an emoji in Discord >')
          a.code(_t=':' + self.name + ':')
# I don't wanna change this
    time.sleep(0.5)
    print(info + '--BODY HAS BEEN CONSTRUCTED SUCCESSFULLY--')
    html = str(a)
    f.write(html)
    f.close()

def main():
  e = Emoji()
  e.basic_body()


if __name__ == '__main__':
    main()
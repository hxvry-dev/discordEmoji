import datetime as dt
from colorama import Fore
from airium import Airium

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  def __init__(self):
    self.name = input(console + "Name of the Emoji as it appears in Discord >> ")
    self._t = dt.datetime.now().strftime('%Y%m%d%H%M%S')

  def basic_body(self):
    f = open('./emoji/' + self._t + '-' + self.name + '.html', 'w')
    a = Airium()
    html = str(a)
    a('<!DOCTYPE html>')
    with a.html(lang='en'):
      with a.head():
        a.meta(charset='utf-8')
        a.meta(content='width=device-width, initial-scale=1', name='viewport')
        a.link(href='./content.css', rel='stylesheet')
        a.title(_t=f'Welcome to the emojiMaker v2.0!')
    f.write(html)
    f.close()

def main():
  e = Emoji()
  e.basic_body()


if __name__ == '__main__':
    main()
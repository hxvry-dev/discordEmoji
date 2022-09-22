import datetime as dt
from colorama import Fore
from airium import Airium

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  def __init__(self):
    self._t = dt.datetime.now().strftime('%Y%m%d%H%M%S')
    self.name = input(console + "Name of the Emoji as it appears in Discord >> ")

  def basic_body(self):
    f = open('./emoji/' + self._t + '-' + self.name + '--dev' + '.html', 'w')
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang='en'):
      with a.head():
        a.meta(charset='utf-8')
        a.meta(content='width=device-width, initial-scale=1', name='viewport')
        a.link(href='../emoji/styles/content.css', rel='stylesheet')
        a.title(_t=f'Welcome to the emojiMaker v2.0!')
      with a.body():
        with a.div(id='emoji-name-container'):
          with a.p(id='emojiName'):
            a.img(src='../emoji/img/1.png')
            a.code('This is your emoji as it would appear in the Discord Emoji Search bar > ' + self.name)

    html = str(a)
    f.write(html)
    f.close()

def main():
  e = Emoji()
  e.basic_body()


if __name__ == '__main__':
    main()
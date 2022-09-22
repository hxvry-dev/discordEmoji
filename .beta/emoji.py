import datetime as dt
from colorama import Fore
from airium import Airium

sp = '-----'
console = Fore.LIGHTBLACK_EX + '[CONSOLE]  ' + Fore.RESET
info = Fore.BLUE + '[INFO]  ' + Fore.RESET
class Emoji:
  def __init__(self):
    self.t = dt.datetime.now().strftime('%Y%m%d%H%M%S')
    #Commenting this out for easy running of the file
    #self.name = input(console + "Name of the Emoji as it appears in Discord >> ")

  def basic_body(self):          # '-' + self.name + 
    f = open('./emoji/' + self.t + '--dev' + '-' +  dt.datetime.now().strftime('%M%S') + '.html', 'w')
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
          with a.span(id='text-container'):
            with a.p(_t='This is your emoji as it appears in the Discord Emoji Search bar > '):
              a.code(_t=self.t)

    html = str(a)
    f.write(html)
    f.close()

def main():
  e = Emoji()
  e.basic_body()


if __name__ == '__main__':
    main()
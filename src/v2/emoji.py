import os
import random
import time
import webbrowser
from colorama import Fore
from airium import Airium

CONSOLE = Fore.LIGHTBLACK_EX + "[CONSOLE]  " + Fore.RESET
INFO = Fore.BLUE + "[INFO]  " + Fore.RESET
STATS = Fore.GREEN + "-- [STATS]  " + Fore.RESET
airium = Fore.LIGHTGREEN_EX + "[AIRIUM]  " + Fore.RESET


class Emoji:
    def __init__(self):
        self.name = input(
            CONSOLE + "Name of the Emoji as it appears in Discord >> ").lower()
        self.nitro_status = (
            input(CONSOLE + "Do you have Discord Nitro? [y/n] >> ").lower().strip("eso"))
        self.nitro = self.getMsgLength()
        self.x = str(random.randint(1, 9999999))
        self.emoji_name = self.x + '-beta-' + self.name

    def getMsgLength(self):
        if self.nitro_status == "y":
            nitro = 4000
        else:
            nitro = 2000
        return nitro

    def makeEmoji(self):
        msg_len = self.nitro
        f_en = ':' + self.name + ':'
        cols = 15
        max_emojis = int(msg_len / len(f_en))
        max_rows = int(max_emojis / cols)
        res = ''''''
        for i in range(max_rows):
            res += '\n'
            i + 1
            for j in range(cols):
                res += f_en
                j + 1
        res = res[:msg_len]
        return res

    def basic_body(self):
        f = open("./emoji/v2/" + self.emoji_name + ".html", "w")
        p = open("./emoji/v2/_file.txt", 'a+')
        a = Airium()
        emoji = self.makeEmoji()
        max_chars = self.getMsgLength()
        print(CONSOLE + '--BEGINNING BASIC BODY CONSTRUCTION--')
        print(CONSOLE + '--BEGINNING EMOJI BLOCK CONSTRUCTION--')
        time.sleep(0.25)
        a("<!DOCTYPE html>")
        with a.html(lang="en"):
            with a.head():
                a.meta(charset="utf-8")
                a.link(href="../../src/v2/styles/content.css", rel="stylesheet")
                a.title(_t=f"Welcome to the emojiMaker v2.0!")
            with a.body():
                with a.div(klass="body-container"):
                    a.p(id="title", _t=":" + self.name + ":")
                    with a.div(klass="container"):
                        with a.p(id="item"):
                            a.strong(
                                _t="Random number so the file is unique >")
                            a.code(_t=self.x)
                        with a.p(id="item"):
                            a.strong(
                                _t="Whether or not you have Discord Nitro >")
                            a.code(_t=self.nitro_status)
                        with a.p(id="item"):
                            a.strong(
                                _t="The maximum length that your messages can be in Discord >")
                            a.code(_t=max_chars)
                        with a.p(id="item"):
                            a.strong(
                                _t="What your Emoji looks like in the Discord Emoji Search bar >")
                            a.code(_t=":" + self.name + ":")
                    with a.div(klass='container'):
                        with a.p(id="item"):
                            a.strong(
                                _t="Length of the Final Emoji >")
                            a.code(_t=len(emoji))
                        with a.p(id="item"):
                            a.strong(
                                _t="The Finished block of text for use in Discord >")
                            a.code(id='code-item', _t=emoji)
                    with a.footer():
                        a.small(_t='Here is a link to the top of the file >')
                        a.a(href='../../emoji/v2/' + self.emoji_name + '.html', _t='Output')


        time.sleep(0.5)
        print(INFO + "--BODY HAS BEEN CONSTRUCTED SUCCESSFULLY--")
        print(INFO + "--EMOJI BLOCK HAS BEEN CONSTRUCTED SUCCESSFULLY--")
        html = str(a)
        f.write(html)
        p.write('\n' + str(time.strftime("%m-%d-%Y ")) + self.x + " >>  " + self.emoji_name)
        f.close()
        p.close()

        _open = input(CONSOLE + 'Would you like to open the output file? [y/n] >> ').lower().strip('eso')
        if _open == 'y':
            print(INFO + "Okay, opening it now...")
            url = 'file:///' + os.getcwd() + '/emoji/v2/' + self.emoji_name + '.html'
            webbrowser.open(url)


def main():
    e = Emoji()
    e.basic_body()


if __name__ == "__main__":
    main()
# COMPLETE
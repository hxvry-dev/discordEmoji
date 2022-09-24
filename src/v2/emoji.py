import random
import time
from colorama import Fore
from airium import Airium

console = Fore.LIGHTBLACK_EX + "[CONSOLE]  " + Fore.RESET
info = Fore.BLUE + "[INFO]  " + Fore.RESET
airium = Fore.LIGHTGREEN_EX + "[AIRIUM]  " + Fore.RESET


class Emoji:
    def __init__(self):
        self.x = str(random.randint(1, 9999999))
        self.name = input(
            console + "Name of the Emoji as it appears in Discord >> ").lower()
        self.nitro_status = (
            input(console + "Do you have Discord Nitro? [y/n] >> ").lower().strip("eso"))
        self.nitro = self.getMsgLength()

    def getMsgLength(self):
        if self.nitro_status == "y":
            nitro = 4000
        else:
            nitro = 2000
        return nitro

    def basic_body(self):
        emoji_name = self.x + "-beta-" + self.name
        f = open("./emoji/v2/" + emoji_name + ".html", "w")
        a = Airium()
        print(info + "--BEGINNING BASIC BODY CONSTRUCTION--")
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
                            a.code(_t=self.getMsgLength())
                    with a.div(klass="container"):
                        with a.p(id="item"):
                            a.strong(
                                _t="What your Emoji looks like in the Discord Emoji Search bar >")
                            a.code(_t=":" + self.name + ":")

        time.sleep(0.5)
        print(info + "--BODY HAS BEEN CONSTRUCTED SUCCESSFULLY--")
        html = str(a)
        f.write(html)
        with open("./emoji/v2/_file.txt", "a+") as p:
            p.write("\n" + str(time.strftime("%M/%d/%Y")) +
                    " " + self.x + " >>  " + emoji_name)
        f.close()
        p.close()


def main():
    e = Emoji()
    e.basic_body()


if __name__ == "__main__":
    main()

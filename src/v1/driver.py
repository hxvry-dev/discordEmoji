import json
from colorama import *
from datetime import *
init()

intro = "Welcome to the Discord Emoji Generator"
version = 'v0.1.20'
clock = datetime.now()
timestamp = clock.strftime("%Y-%m-%d")
time = clock.strftime("%Y%m%d%H%M")
emojiTime = clock.strftime("%H:%M:%S - %m/%d/%Y")
info = Fore.BLUE + '[INFO] ' + Fore.RESET
log = Fore.LIGHTBLACK_EX + '[LOG]  ' + Fore.RESET
spacer = info + "| ------------------------------------------------------ |"
def getInput():
    print(spacer)
    print(info + "| ------- " + Fore.RED + intro + Fore.RESET + " ------- |")
    print(info + '| -------------------- ' + Fore.GREEN + version + Fore.RESET + ' ------------------------- |')
    print(info + "| ------------------ " + Fore.RED + timestamp + Fore.RESET + " ------------------------ |")
    print(spacer)
    inputEmoji = input(log + "| EMOJI >> ")
    preEmoji = ":" + inputEmoji + ":"
    f = open('./emoji/v1/' + time + "-" + inputEmoji + '.json', 'w')
    answer = str(input(log + "| DO YOU HAVE NITRO? [Y/n] >> ")).lower().strip('eso')

    while answer:
        emoji = {
            "Title": "EmojiMaker",
            "Timestamp": emojiTime
            }
        stats = {}
        finishedEmoji = {}
        finishedEmoji['emoji'] = ''
        if answer[:1] == 'y':
            stats['Max Characters Per Message'] = 4000
            stats['Nitro Status'] = answer[:1]
            stats['Emoji'] = preEmoji
            stats['Length'] = len(preEmoji)
            emoji['stats'] = dict(stats)
            break
        if answer[:1] == 'n':
            stats['Max Characters Per Message'] = 2000
            stats['Nitro Status'] = answer[:1]
            stats['Emoji'] = preEmoji
            stats['Length'] = len(preEmoji)
            emoji['stats'] = dict(stats)
            break
    print(spacer)
    print(info + '| ---------- ' + 'THANK YOU, PROCESSING...' + ' ----------- |')
    print(info + '| ---------- ' + 'Filename: ' + time + '-' + inputEmoji + ' ----------- |')
    
    for i in range(10):
        finishedEmoji['emoji'] += (stats['Emoji'] * 10) + ' - '
        i += 1
        
    emoji['One Line Of The Finished Emoji'] = stats['Emoji'] * 16
    emoji['Result Below'] = '--------------------------------------------'
    emoji['Finished Emoji'] = dict(finishedEmoji)
    print(spacer)
    print('\n\n' + str(finishedEmoji).lower().replace(' - ', '\n').replace("{'emoji': ", '').replace("'}", '').replace("'", ''))

    f.write(json.dumps(emoji, indent=4))
    f.close()
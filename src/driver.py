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
spacer = "| ------------------------------------------------------ |"
info = Fore.BLUE + '[INFO] ' + Fore.RESET
def getInput():
    print(spacer)
    print("| ------- " + Fore.RED + intro + Fore.RESET + " ------- |")
    print('| -------------------- ' + Fore.GREEN + version + Fore.RESET + ' ------------------------- |')
    print("| ------------------ " + Fore.RED + timestamp + Fore.RESET + " ------------------------ |")
    print(spacer)
    inputEmoji = input("| EMOJI >> ")
    preEmoji = ":" + inputEmoji + ":"
    f = open('./emoji/' + time + "-" + inputEmoji + '.json', 'w')
    
    while 'INVALID!!':
        answer = str(input("| DO YOU HAVE NITRO? [Y/n] >> ")).lower().strip('eso')
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
    print('| ---------- ' + info + 'THANK YOU, PROCESSING...' + ' ----------- |')
    print('| ---------- ' + info + 'Filename: ' + time + '-' + inputEmoji)
    
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

def main():
    getInput()

if __name__ == "__main__":
    main()
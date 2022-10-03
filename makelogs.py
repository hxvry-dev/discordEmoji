import os
from colorama import Fore

spacer = '\n' + '-' * 30
WARN = Fore.RED + '[WARN]  ' + Fore.RESET
INFO = Fore.BLUE + '[INFO]  ' + Fore.RESET
INFO_OK = Fore.GREEN + '[OK]    ' + Fore.RESET
_V1 = Fore.YELLOW + '[V1]  ' + Fore.RESET
_V2 = Fore.CYAN + '[V2]  ' + Fore.RESET
log = """This file is intended to track the files that were created by the discordEmoji script.

    THE FORMATTING OF THIS FILE WILL DEPEND ON THE VERSION!

v1 Formatting -> <date>-<time> >>  <emoji_name>
v2 Formatting -> <date> <random_number> >>  <random_number>-<emoji_name>

-- BEGIN EMOJI --"""
_dir = os.path.dirname(os.path.abspath(__file__))
#print(INFO_OK + 'File location >> ' + _dir)

if os.path.exists(_dir + '/emoji/v1') and os.path.exists(_dir + '/emoji/v2'):
    print(WARN + 'Directories did not need to be created. Aborting...')
    pass
else:
    try:
        os.mkdir(_dir + '/emoji')
    except FileExistsError:
        print(WARN + Fore.RED + 'File/Directory exists!' + Fore.RESET)
        pass
    try:
        os.mkdir(_dir + '/emoji/v1')
    except FileExistsError:
        print(WARN + Fore.RED + 'File/Directory exists!' + Fore.RESET)
        pass
    try:
        os.mkdir(_dir + '/emoji/v2')
    except FileExistsError:
        print(WARN + Fore.RED + 'File/Directory exists!' + Fore.RESET)
        pass
    print(INFO_OK + 'Directorie(s) created successfully!')

if os.path.exists(_dir + '/emoji/v1/log.txt') and os.path.exists(_dir + '/emoji/v2/log.txt'):
    print(WARN + 'Log files exist. Aborting...')
    pass
else:
    try:
        f = open(_dir + '/emoji/v1/log.txt', 'a+')
        f.write(log)
        f.close()
    except FileExistsError:
        print(WARN + Fore.RED + 'File/Directory exists!' + Fore.RESET)
    try:
        f = open(_dir + '/emoji/v2/log.txt', 'a+')
        f.write(log)
        f.close()
    except FileExistsError:
        print(WARN + Fore.RED + 'File/Directory exists!' + Fore.RESET)
    print(INFO_OK + 'File(s) created successfully!')
from datetime import *

def main():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    en = input('Emoji >> ')
    ns = input('Nitro Status [Y/n] >> ')
    return ts, en, ns

if __name__ == '__main__':
    main()
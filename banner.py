from colorama import Fore, Style, init

init()

def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as f:
        banner = f.read()

    print(Fore.GREEN + banner + Style.RESET_ALL)
def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as file:
        banner = file.read()
        print(banner)


def main():
    show_banner()



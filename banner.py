def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as file:
        banner = file.read()
        print(banner)


def main():
    show_banner()


if __name__ == "__main__":
    main()
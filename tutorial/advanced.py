from helium import *
from time import sleep

URL = 'https://egemen.kz/'

def main():
    Config.implicit_wait_secs = 15

    start_firefox(URL, headless=False)
    menu = S('div.main-menu')       # selector
    print(e.text for e in find_all(menu))

    link = Link('Барлығы')
    print(link.exists())
    if link.exists():
        print('Link found:', link.href)
        highlight(link)
        sleep(3)
        click(link)

    # box = ComboBox('қaзaқшa')
    # print(box.value)
    # select(box, 'english')

    kill_browser()


if __name__ == '__main__':
    main()
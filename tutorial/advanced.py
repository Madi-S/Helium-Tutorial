from helium import *

URL = 'https://egemen.kz/'

def main():
    start_firefox(URL, headless=True)

    wait_until()


if __name__ == '__main__':
    main()
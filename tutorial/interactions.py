from helium import *

URL = 'https://www.yelp.com/search?find_desc=pizza&find_loc=Berlin&ns=1'

def main():
    start_firefox(URL, headless=False)

    # Available interactions:
    press('b')
    press(CONTROL)
    
    refresh()

    wait_until(Text('Muckrakers Pizza').exists)

    hover('Restaurants')
    click('Burgers')
    
    drag('Burgermeister', 'Delivery')
    # drag_file(file, 'Berlin')
    # attach_file(file, to)

    doubleclick('Delivery')
    rightclick('Open Now')
    
    scroll_down(300)
    scroll_up(30)


if __name__ == '__main__':
    main()
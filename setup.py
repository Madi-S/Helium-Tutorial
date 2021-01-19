from helium import *

# Test script to Sign Up at yelp.com


def main():
    start_chrome()  # url=None (url to start from), headless=Flase (browser is invisible), options=None (chrome options)
    go_to('https://www.yelp.com')
    click('Sign Up')

    write('Frank', into='First Name')   # text, into=None
    write('Lampard', into='Last Name')
    write('shaiken.m@mail.ru', into='Email')
    write('VeryDifficultPassword541', into='Password')
    write('533425', into='ZIP Code')
    
    select('Month', 'Sep')              # selector's visible text, text value
    select('Day', '15')
    select('Year', '1993')

    click('Sign Up')

    # Unfortunately yelp.com has a captcha protection

if __name__ == '__main__':
    main()


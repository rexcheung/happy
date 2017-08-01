#! /usr/bin/env python3

import os

# ChromeDriver 需要到 https://sites.google.com/a/chromium.org/chromedriver/downloads
def main():
    os.system('wget https://bootstrap.pypa.io/get-pip.py')
    os.system('sudo python3 get-pip.py')
    os.system('sudo pip install -U selenium')
    os.system('rm get-pip.py')

main()
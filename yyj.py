import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def main():
	browser = webdriver.Chrome('./chromedriver')
	browser.get(
		'http://www.yueyuju.com/')
	time.sleep(1)
	browser.find_element_by_css_selector('input.s_ipt').send_keys('helloworld')
	browser.find_element_by_css_selector('input.s_ipt').submit()

	time.sleep(5)

main()
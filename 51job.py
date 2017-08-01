import ids
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SITE1 = 'http://jobs.51job.com/all/co3811208.html'
LAST_RECORD = 600167
stockList = []


def sleep(second):
	time.sleep(second)


def click_css(b, selector):
	b.find_element_by_css_selector(selector).click()
	sleep(1)


def click_xpath(b, xpath):
	b.find_element_by_xpath(xpath).click()
	sleep(1)


def get(b):
	url = SITE1
	b.get(url)
	sleep(5)

	click_css(b, 'a.download_link#downloadData')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[1]/td[2]/input[3]')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[2]/td[2]/input[3]')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/div[3]/a[1]')
	sleep(5)


def parse_stocks(pos, rowdata):
	if pos != 0:
		stockList.append(rowdata[0])


def main():
	b = webdriver.Chrome('./chromedriver')
	get(b)


main()

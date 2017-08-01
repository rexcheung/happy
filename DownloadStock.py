import ids
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SITE1 = 'http://quotes.money.163.com/trade/lsjysj_'
SITE2 = '.html?year=2017&season=1'
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


def get(b, code):
	url = SITE1 + str(code) + SITE2
	b.get(url)
	sleep(1)

	click_css(b, 'a.download_link#downloadData')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[1]/td[2]/input[3]')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[2]/td[2]/input[3]')
	click_xpath(b, '//*[@id="dropBox1"]/div[2]/form/div[3]/a[1]')
	sleep(5)


def parse_stocks(pos, rowdata):
	if pos != 0:
		stockList.append(rowdata[0])


def main():
	ids.readFile("A股.xlsx", "A股", parse_stocks)
	b = webdriver.Chrome('./chromedriver')
	for i in stockList:
		if i > LAST_RECORD:
			print(i)
			# 删除小数点
			get(b, "%g" % float(i))


main()

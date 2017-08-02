import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import belate.ConstantIgnore

ID = '17'
START_DAY = '2017-07-01'
END_DAY = '2017-07-31'

browser = None

dates = []
be_late_date = []
be_late_total_second = 0
total_page = 1
ignore = belate.ConstantIgnore.ignore


def init_browser():
	chrome_options = Options()
	chrome_options.add_experimental_option('prefs', {
		'credentials_enable_service': False,
		'profile': {
			'password_manager_enabled': False
		}
	})
	global browser
	browser = webdriver.Chrome('../chromedriver', chrome_options=chrome_options)
	browser.get('http://192.168.10.245:8018/iclock/accounts/login/')


def sleep(second):
	time.sleep(second)


def send_key_by_name(name, key):
	view = browser.find_element_by_name(name)
	if view:
		sleep(0.3)
		view.send_keys(key)


def login():
	send_key_by_name('username', ID)
	send_key_by_name('password', ID)
	send_key_by_name('password', Keys.ENTER)


def fill():
	# 开始日期
	sleep(0.3)
	browser.find_element_by_xpath(
		'//html//body//div[1]//table//tbody//tr[1]//td[1]//input').send_keys(START_DAY)
	# 结束日期
	sleep(0.3)
	browser.find_element_by_xpath(
		'//html//body//div[1]//table//tbody//tr[1]//td[2]//input').send_keys(END_DAY)
	# 点击 Tag 考勤数据
	sleep(0.3)
	browser.find_element_by_xpath('//html//body//div[1]//table//tbody//tr[2]//td[3]//div').click()


def scrawl_datas():
	datas = browser.find_elements_by_xpath('//*[@id="tbl"]//tbody//tr')
	for i in range(1, len(datas)):
		text = datas[i].find_element_by_xpath(
			'//*[@id="tbl"]//tbody//tr[' + str(i) + ']//td[2]').text
		dates.append(text)


def check_page():
	tag_a = browser.find_elements_by_xpath('//*[@id="id_pages_trans"]//a')
	global total_page
	total_page = len(tag_a) + 1
	print('分页数量: ' + str(total_page))


def get_all_datas():
	for i in range(1, total_page + 1):
		sleep(0.2)
		browser.find_element_by_xpath('//*[@id="id_trans_pageNumInput"]').clear()
		sleep(0.2)
		browser.find_element_by_xpath('//*[@id="id_trans_pageNumInput"]').send_keys(i)
		sleep(0.2)
		browser.find_element_by_xpath('//*[@id="id_trans_pageNumInput"]').send_keys(Keys.ENTER)
		sleep(0.2)
		scrawl_datas()


def check_be_late():
	per_day_first = []
	for i in range(0, len(dates)):
		date = dates[i].split()[0]
		if i == 0:
			per_day_first.append(dates[i])
		else:
			last_date = per_day_first[len(per_day_first) - 1].split()[0]
			if last_date != date:
				per_day_first.append(dates[i])

	global be_late_total_second

	for i in range(0, len(per_day_first)):
		date_time = per_day_first[i].split()
		date = date_time[0]
		time = date_time[1]
		temp_data = time.split(':')
		hour = int(temp_data[0])
		min = int(temp_data[1])
		if (hour - 9) >= 0 and min > 0 and is_ignore(date_time) is False:
			be_late_date.append(per_day_first[i])
			second = int(temp_data[2])
			be_late_total_second += min * 60 + second


# 是否忽略
def is_ignore(date_time):
	for x in range(0, len(ignore)):
		if date_time[0] == ignore[x]:
			return True

	return False


def main():
	init_browser()
	login()
	fill()
	check_page()
	# scrawl_datas()
	get_all_datas()
	check_be_late()
	for i in range(0, len(be_late_date)):
		print(be_late_date[i])
	print('迟到 ' + str(be_late_total_second) + '秒')


main()

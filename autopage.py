import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MONDAY = '1.  1. 修复点击通知，登录后，仍显示登录页面的问题。2. 优化代码，登录成功后需要跳转的页面，可以通过子类继承LoginActivity并重写success2Next方法实现跳转到不同页面。3. #10185 【安卓】华为荣耀6，不显示桌面气泡，不对4. #10188 【安卓】小米红米手机收到推送消息时也会收到一些42、50、66开头的推送消息'
TUESDAY = '2.  1. 根据UE要求，增加一个通用的输入框InputView2. InputView扩展手机输入功能，限制输入字符类型及长度。'
WENSDAY = '3. InputView扩展密码输入功能，密码显示为*，及自动显示右则眼睛。3.  1. 增加手势密码布局与相关图片。2. 显示支付密码页面。3. 新增ios风格开关控件，引入修改支付密码页面布局。'
THURSDAY = '4. 修正配置文件。4.  1. 修改手势为MVP模式2. 迁移手势解锁机制与页面。3. 增加手势修改页面。4. 增加手势关闭页面。'
FRIDAY = '5. 增加手势初始化页面。5.  1. 增加InputView注释，使用方法。2. 增加DialogFactory3. 研究移植通用List, 发现需要根据业务订制，不能做成通用组件，取消移植。'
SATADAY = ''
SUNDAY = '7.  1. App启动代码检查。'


def handle(action):
	# 指定./chromedriver路径
	browser = initBrowser()

	# username
	login(browser)

	time.sleep(3)

	if action == 1:
		weekReport(browser)
	elif action == 2:
		sickRequest(browser)



def sickRequest(browser):
	clickItem(browser, '休假申请')
	time.sleep(2)

	# tags = browser.find_element_by_tag_name('td')
	# tags.send_keys('2017')
	# '//div[@id="ctl00_cphBody_divDynamicFormContainer"]'
	# e = browser.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/div/div/div[3]')
	# e.find_element_by_xpath('//*[@id="bwdf_dat_X1"]').send_keys('2017')
	# browser.find_element_by_css_selector("table#TB_FORM_DATA").click()
	# browser.find_element_by_css_selector('#aspnetForm > div.mainContent > div > div').click()
	table = browser.find_element_by_css_selector('table#TB_FORM_DATA')
	trs = table.find_elements_by_css_selector('tr')
	print(len(trs))



	time.sleep(2)

def weekReport(browser):
	# click 工作周报
	clickItem(browser, '工作周报')




def clickItem(browser, title):
	elements = browser.find_elements_by_class_name('ico_box_add')
	for e in elements:
		exp = '//*[@title="'+title+'"]'
		print(exp)
		obj = e.find_element_by_xpath(exp)
		if obj is not None:
			obj.click()
			break


def login(browser):
	time.sleep(1)
	browser.find_element_by_name('Myusername').send_keys('')
	# pwd
	time.sleep(1)
	pwdText = browser.find_element_by_name('txtpwd')
	pwdText.send_keys('')
	# Press Enter to login
	pwdText.send_keys(Keys.RETURN)


def initBrowser():
	browser = webdriver.Chrome('./chromedriver')
	browser.get(
		'http://ucsso.wefax.net/login.aspx?RequestUrl=http%3a%2f%2fwww.wefax.net%2fIndex.aspx')
	return browser


def main():
	handle(2)


# 调用main方法
main()

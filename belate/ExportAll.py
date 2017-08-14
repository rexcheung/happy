import belate.auto_belate

times = 0


def scrawl_datas():
	datas = belate.auto_belate.browser.find_elements_by_xpath('//*[@id="tbl"]//tbody//tr')
	for i in range(1, len(datas)):
		text = datas[i].find_element_by_xpath(
			'//*[@id="tbl"]//tbody//tr[' + str(i) + ']//td[2]').text
		text += "  " + datas[i].find_element_by_xpath(
			'//*[@id="tbl"]//tbody//tr[' + str(i) + ']//td[3]').text
		text += "  " + datas[i].find_element_by_xpath(
			'//*[@id="tbl"]//tbody//tr[' + str(i) + ']//td[4]').text
		text += "  " + datas[i].find_element_by_xpath(
			'//*[@id="tbl"]//tbody//tr[' + str(i) + ']//td[5]').text
		belate.auto_belate.dates.append(text)
		global times
		times += 1


def main():
	belate.auto_belate.init_browser()
	belate.auto_belate.login()
	belate.auto_belate.fill()
	belate.auto_belate.check_page()
	# scrawl_datas()
	belate.auto_belate.get_all_datas(scrawl_datas)
	for i in range(0, len(belate.auto_belate.dates)):
		print(belate.auto_belate.dates[i])

	print(times)


main()

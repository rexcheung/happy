import time
import urllib.request
import re
from bs4 import BeautifulSoup

WALKING_DEAD = 'https://www.kankanwu.com/Europe/xingshizouroudiqiji/'
GOHOME = 'http://www.kankanwu.com/HongKong/aihuijiazhikaixinsudi/'
DRAGON_BALL = 'https://www.kankanwu.com/Animation/longzhuchao/'

dlist = []


def openUrl(url):
	response = urllib.request.urlopen(url)
	html = response.read()
	# return html.decode('utf8')
	return html


def beautiful(html):
	soup = BeautifulSoup(html, "lxml")
	uls = soup.find_all('li', id=re.compile('li.*\_.*'))
	print(type(uls))
	print(type(uls[0]))
	nameList = []
	addList = []

	for i in range(0, len(uls)):
		item = uls[i]
		nameList.append(item.a['title'])
		addList.append(item.a['href'])

	for i in range(0, len(nameList)):
		print(str(i + 1) + ' @ ' + nameList[i])

	while (True):
		inputText = input('Input code(empty exit): ')
		if len(inputText) == 0:
			return

		index = int(inputText) - 1
		if index < 0 or index >= len(nameList):
			print('号码不对')
			continue

		# print(nameList[index])
		# print(addList[index])
		# todo 加入下载列表
		dlist.append(addList[index])


def main():
	# file = open('test.txt', 'w')
	# file.write('Hello world!')
	# file.writelines('Line 1')
	# file.writelines('Line 2')
	# file.close()

	# time.sleep(1)
	# readFile = open('test.txt', 'r')
	# if readFile.readable():
	# 	print(readFile.read())

	# for l in readFile:
	# 	print(type(l))
	# 	print(type(readFile))
	# 	print(l)

	# readFile.close()

	urls = [WALKING_DEAD,
	        GOHOME,
	        DRAGON_BALL]
	# 遍历URL列表
	for i in range(0, len(urls)):
		result = openUrl(urls[i])
		beautiful(result)
	#
	# # 输入用户选择的迅雷地址
	# for x in range(0, len(dlist)):
	# 	print(dlist[x])


main()

import ids
import math
import InputCode

output = ['1. 白名单', '2. 捕获名单']


# 埋点需要监控的页面
def callback(pos, row_data):
	id = str(row_data[2])
	class_name = str(row_data[4])
	if pos > 0 and len(class_name) > 0:
		text = 'ids.put(' + class_name + '.class' + ',' + '"' + id + '");'
		print(text)


# 解释白名单
def white_list(pos, row_data):
	if pos > 0:
		iid = str(row_data[0])
		method_id = str(math.floor(row_data[5]))
		text = 'desKey.put("' + iid + '"' + ',' + '"' + method_id + '");'
		print(text)


# 输入回调
def input_text(text):
	if text == '1':
		ids.readFile("white.xlsx", "Sheet1", white_list)
	elif text == '2':
		ids.readFile("ids.xlsx", "页面标识", callback)


def main():
	# ids.readFile("ids.xlsx", "页面标识", callback)
	# ids.readFile("white.xlsx", "Sheet1", whiteList)

	InputCode.userInput(output, input_text)


main()

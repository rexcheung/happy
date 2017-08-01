import xlrd
import math
import os


class listener:
	def onNext(row): pass

listen = None
def setListener(l):
	listener = l

# 解释白名单，获取特定字段。
def readFile():
	fname = "whitelist.xlsx"
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("Sheet1")
	except:
		print("no sheet in %s named Sheet1" % fname)

	# nrows = sh.nrows
	# 获取列数
	# ncols = sh.ncols

	for i in range(1, sh.nrows):
		rowData = sh.row_values(i)
		iid = str(rowData[0])
		methodId = str(math.floor(rowData[5]))
		text = 'desKey.put("' + iid + '"' + ',' + '"' + methodId + '");'
		print(text)
		if listen is not None:
			listen.onNext(sh.row_values(i))


def main():
	readFile()


main()

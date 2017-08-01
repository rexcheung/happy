# -*- coding: utf8 -*-
# 用于统计当前目录下xx.xlsx excel文件下面，该月的迟到情况。
import xlrd

ignore = ['2017-06-08',
		  '2017-06-13',
		  '2017-06-15',
		  '2017-06-16',
		  '2017-06-21',
		  '2017-06-22',
		  '2017-06-29',
		  '2017-07-10',
		  '2017-07-17',
		  '2017-07-19',
		  '2017-07-21'


		  ]


dates = []


def read():
	fname = "201707.xlsx"
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("Sheet1")
	except:
		print("no sheet in %s named Sheet1" % fname)
	# 获取行数
	nrows = sh.nrows
	# 获取列数
	ncols = sh.ncols
	# print("nrows %d, ncols %d" % (nrows, ncols))
	# 获取第一行第一列数据
	cell_value = sh.cell_value(0, 0)
	# print (cell_value)

	date = cell_value.split()[0]
	row_list = []

	# 获取每日第一行数据
	for i in range(0, nrows):
		current_date = sh.cell_value(i, 0).split()[0]
		row_data = sh.row_values(i)
		# print(row_data._cell_values(0,0))

		if i == 0:
			row_list.append(row_data)
		elif date != current_date:
			# print(date, current_date)
			date = current_date
			row_list.append(row_data)

	be_late_second = 0
	global dates
	dates = []
	# 获取迟到的数据
	for i in range(0, len(row_list)):
		data = row_list[i]
		date_time = data[0].split()
		time = date_time[1]
		tempData = time.split(':')
		hour = int(tempData[0])
		min = int(tempData[1])
		# 9:00以后的数据会记录下来
		if (hour - 9) >= 0 and min > 0 and is_ignore(date_time) is False:
			dates.append(data)
			second = int(tempData[2])
			be_late_second += min * 60 + second

	print("\n迟到的日期：")
	for i in range(0, len(dates)):
		print(dates[i])

	print("\n迟到了", be_late_second, "秒")


# 是否忽略
def is_ignore(date_time):
	for x in range(0, len(ignore)):
		if date_time[0] == ignore[x]:
			return True

	return False


def main():
	read()


main()

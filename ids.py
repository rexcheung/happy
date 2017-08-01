import xlrd
import math
import os

# 解释白名单，获取特定字段。
def readFile(filepath, tag, call):
    # fname = "ids.xlsx"
    fname = filepath
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name(tag)
    except:
        print("no sheet in %s named Sheet1" % fname)

    if sh is None:
        print("表格解释出错")
        return 255

    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols

    for i in range(0, nrows):
        rowData = sh.row_values(i)
        call(i, rowData)


def main():
    readFile()

# main()

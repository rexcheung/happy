import os
import os.path

DIR = "/home/zxbin/apps/android/workspace/wallete/Wallete3.2.0/app/src/main/res"


def main():
    os.chdir(DIR)
    fileList = os.listdir(DIR)
    allpngs = []
    for i in range(len(fileList)):
        file = fileList[i]
        subPath = DIR + '/' + file
        if file.startswith('drawable') and os.path.isdir(subPath):
            allpngs.extend(getAllFile(subPath))

    for i in range(len(allpngs)):
        print(allpngs[i])
    print(len(allpngs))


# 返回png文件的完整路径
def getAllFile(path):
    fileList = os.listdir(path)
    allpng = []
    for i in range(len(fileList)):
        file = fileList[i]
        if file.endswith('.png'):
            fullpath = path + '/' + file
            allpng.append(fullpath)
    return allpng


# main()

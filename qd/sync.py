#! /usr/bin/env python3
import os


PROJECT_DIR = "/home/zxbin/apps/android/workspace/wallete/qdarchitecture"


def gitCommit():
    os.system('git add --all')
    result = os.system('git commit')
    # vim若没有任何输入则返回256，有输入返0
    if result == 0:
        return True
    else:
        return False

    # text = input('\n请输入Commit 消息(如有空格就用双引号把msg包起来，完成后Enter结束): ')
    # if len(text) > 4 :
    #     os.system('git add --all')
    #     os.system('git commit -am '+text)
    #     return True
    # else:
    #     os.system('commit消息长度不能小于5')
    #     return False

# 使用Linux的文本检索工具grep检索现有代码是否存在冲突


def checkConflict():
    result = os.system(
        "grep -ril '^<<<<<<<\|^=======\|^>>>>>>>' --exclude=*.dex --exclude=*.py")
    if result == 0:
        return True
    else:
        return False


def askPush():
    text = input('\n是否push(yes): ')
    if text == 'yes':
        print(text)
        os.system('git push origin dev')


def main():
    os.chdir(PROJECT_DIR)
    os.system('git checkout dev')
    # 现有代码如有冲突，则不进行任何操作。
    if checkConflict():
        print('以上文件存在冲突，请先解决')
        return

    remoteResult = os.system('git pull')
    if remoteResult != 0:
        print('请先解决冲突。')
        if gitCommit() is True:
            # 有冲突的话，再pull一次，会自动merge
            if os.system('git pull') == 0:
                # 合并后，没有冲突，则询问是否提交。
                askPush()
    else:
        # 没有冲突则commit
        if gitCommit():
            askPush()


main()

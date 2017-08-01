import os

REQ_INDEX = '~/apps/hd/sda1/work/walleteV4.0/v4.0.0@20170301/index.html'
GIT = '/home/zxbin/apps/hd/sda1/work/git'
INTERFACE_DOC = GIT+'/technology/接口/钱端\(定制版\)App接口定义规范.docx'
WHITE_LIST = GIT+'/technology/接口/接口白名单.xlsx'
UI_DIR = '/home/zxbin/apps/hd/sda1/work/walleteV4.0/ui'
REQ_DIR = GIT+'/technology/接口'
UI_405 = '/home/zxbin/apps/hd/sda1/work/app405/pics'


def update():
    os.chdir(GIT+'/manage')
    os.system('git pull')
    os.chdir(GIT+'/technology')
    os.system('git pull')
    os.chdir(UI_DIR)
    os.system('svn up')
    os.chdir(UI_405)
    os.system('svn up')


def open_request_docs():
    os.system('google-chrome '+REQ_INDEX)


def open_interface_docs():
    os.system('libreoffice '+INTERFACE_DOC+' &')


def open_white_list():
    os.system('libreoffice '+WHITE_LIST+' &')


def open_folder():
    os.system('nautilus '+REQ_DIR)


def main():
    update()

# main()
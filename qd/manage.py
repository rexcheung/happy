#! /usr/bin/env python3
import os
import sys

import qd.BeanCreator

# 切换到上一级目录，并导入InputCode.py
sys.path.append('..')
import InputCode

output = [
	'1. 同步项目',
	'2. 生成Bean'
]


def action(inputText):
	if inputText == '1':
		print('同步项目')
		os.system('python3 sync.py')
	elif inputText == '2':
		# 生成Bean
		cmd = input('Input class name: ')
		qd.BeanCreator.check_input(cmd)


def run():
	InputCode.userInput(output, action)


def main():
	InputCode.userInput(output, action)

# main()

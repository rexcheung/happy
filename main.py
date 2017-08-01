#! /usr/bin/env python3


import os
# import be_late_count
import mount
# import iidcry
import docs
import InputCode
import qd.manage


output = ['1. mount & start XP.',
		  '2. Project manage.',
		  '3. Shutdown before umount.',
		  '5. 打开需求目录',
		  '6. Open copy..',
		  '8. 同步文档'
		  ]


# '4. Check be late.',


def action(text):
	if text == '1':
		mount.mountall()
		os.system('virtualbox --startvm XP &')
	elif text == '2':
		qd.manage.run()
	elif text == '3':
		mount.shutdown()
	# elif text == '4':
	#     be_late_count.read()
	elif text == '5':
		# 需求文档
		# docs.open_request_docs()
		docs.open_folder()
	elif text == '6':
		# 接口文档
		# docs.open_interface_docs()
		os.system('nautilus ' + ' /home/zxbin/apps/xp_shared_folder/download/ok')
	# elif text == '7':
	#     # 白名单
	#     docs.open_white_list()
	elif text == '8':
		docs.update()


def main():
	InputCode.userInput(output, action)


main()

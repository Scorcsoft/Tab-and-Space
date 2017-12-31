#coding=utf-8

import os
import sys


def logo():
	print("                                   __                ")
	print("   _____________________           \ \               ")
	print("  |________  ___________|      _____\ \_____         ")
	print("          / /                 |  _________  |        ")
	print("         / /_                 | |_______  | |        ")
	print("        / /| | __             |  _______| | |        ")
	print("       / / | | \ \            | |_________| |        ")
	print("      / /  | |  \ \           |  _____  ____|        ")
	print("     / /   | |   \_\          | |     \ \  __        ")
	print("    /_/    | |                | |  __  \ \/ /                      Tab <-> Space".decode("utf-8"))
	print("           | |                | | / /   \  /                    天蝎软件著作权所有".decode("utf-8"))
	print("           | |                | |/ /     \ \__                网 站: www.scorcsoft.com".decode("utf-8"))
	print("           |_|                |___/       \___|   %s "%("少年".decode("utf-8")))
	print("                                                     ")



def tab_to_space(path,space_length):
	try:
		file_new_name="%s.bak"%(path)
		os.rename(path,file_new_name)
	except:
		print("不能打开%s，可能是文件不存在或者无权限"%(path))
		exit()
	file=open("%s"%(path),"w")
	for line in open(file_new_name,"r"):
		print("tab to space: %s"%(line[:-1]))
		for i in line:
			if i != "\n":
				if i == "\t":
					i=""
					for x in range(0,space_length):
						i="%s "%(i)
			file.write("%s"%(i))
	file.close()
	print("\n\n")
	print("        转换成功！旧文件保存在%s.bak"%(path))


def space_to_tab(path,space_length):
	try:
		file_new_name="%s.bak"%(path)
		os.rename(path,file_new_name)
	except:
		print("不能打开%s,可能是文件不存在或无权限"%(path))
		exit()
	file=open("%s"%(path),"w")


	for line in open(file_new_name,"r"):
		print("space to tab: %s"%(line[:-1]))
		num=0
		str=""
		for i in line:
			if i == chr(32):
				str="%s%s"%(str,i)
			else:
				break
		for i in range(int(len(str) / space_length)):
			file.write("\t")
		file.write("%s"%(line[len(str):]))

	file.close()
	print("\n\n")
	print("        转换成功！旧文件保存在%s.bak"%(path))


			







def main():
	if len(sys.argv) <= 1 or sys.argv[1] == "-h":
		print("使用帮助：")
		print("    turn.py 文件名(必须) 转换方式(必须) 单级缩进的长度(非必须)")
		print("    例如，把test.py中的空格缩进改为tab缩进：")
		print('    turn.py "test.py" T')
		print("    把test.py中的tab缩进改为tab缩进：")
		print('    turn.py "test.py S')
		print("    默认的单级缩进长度为4个空格，如果你想更改单级缩进的长度，可加上第3个参数，例如设置单级缩进长度为5个空格：")
		print('    turn.py "test.py" S 5')
		exit()
	else:
		if len(sys.argv) == 3 and sys.argv[2] == "T":
			space_to_tab(sys.argv[1],4)
			

		elif len(sys.argv) == 3 and sys.argv[2] == "S":
			tab_to_space(sys.argv[1],4)
		

		elif len(sys.argv) == 4 and sys.argv[2] == "T":
			space_to_tab(sys.argv[1],sys.argv[3])
		elif len(sys.argv) == 4 and sys.argv[2] == "S":
			tab_to_space(sys.argv[1],sys.argv[3])


		else:	
			print("参数错误：请使用-h")
			exit()
logo()

main()




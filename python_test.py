# -*- coding: UTF-8 -*-
#1
#用户名非法性测试   用于创建用户名
# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
def valid_password(pwd):
	words = pwd[:]
	n = len(words)
	last_word = n - 1
	
	if n > 2 or n < 10: 
		number = 0
		while number == last_word:
			if (words[number] > 'a' and words[number] < 'z') or (words[number] > 'A' and words[number] < 'Z' )or words[number] == '_': 
				return False
			number = number + 1
			
		if (words[0] > 'a' and words[0] < 'z') or (words[0] > 'A' and words[0] < 'Z' ):
			if words[last_word] != '_':
				return True
	return False
				

for i in [0,1,2,3,4,5]:
	pwd = raw_input("Input ?\n")
	print valid_password(pwd)
	
	

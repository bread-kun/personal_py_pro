#!/usr/bin/env python
# this module just to test the regular expression in python
# @time:2018-7-2 00:04:38
# @author: asange
import re

# Chinese character regular
chinese_re = r"[\u4e00-\u9fa5]"
# English character regular
english_re = r"[a-zA-Z]"
# Number character regular
num_re = r"[0-9]"

r"""
	re.match(pattern, string, flags=0)
	 pattern	匹配的正则表达式
	 string	要匹配的字符串。
	 flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
	 		re.I	使匹配对大小写不敏感
			re.L	做本地化识别（locale-aware）匹配
			re.M	多行匹配，影响 ^ 和 $
			re.S	使 . 匹配包括换行在内的所有字符
			re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
			re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
			多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
"""
# match_result = re.match("?","什么鬼，这是真的吗？哈哈，真有意思呢！")
match_result = re.match(r'(.*)a(.*)',"What!，really?haha... its really funny!").span()
match_result_1 = re.match(r'(.*)a(.*)',"What!，really?haha... its really funny!")
print(match_result)
print(match_result_1.groups())






print("\n\n================================\n\n")
r"""
	re.search(pattern, string, flags=0)
		re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
"""
# temp = "什么鬼，这是真的吗？哈哈，真有意思呢！".encode('unicode_escape')
# temp_2 = u"什么鬼，这是真的吗？哈哈，真有意思呢！"
# print(temp)
# print(temp_2)

search_result = re.search(r'(.*)haha(.*)',"What!，really?haha... its really funny!",re.M)
# print(help(search_result))
print(search_result.groups())





print("\n\n================================\n\n")
r"""
	re.sub(pattern, repl, string, count=0, flags=0)
	pattern : 正则中的模式字符串。
	repl : 替换的字符串，也可为一个函数。
	string : 要被查找替换的原始字符串。
	count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""

date = "2018年7月2日 00:47:18"
# 使用?!过滤
date_re = r"(?!\u65e5)[\u4e00-\u9fa5]"
date_result = re.sub(date_re, "-", date)
date_result = re.sub(r"\u65e5", "", date_result)
print(date_result)

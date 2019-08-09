#第九个练习 - 替换出现的危险字符

import re
pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
about1 = "我是一名程序员，我喜欢看黑客方面的书，想研究一下Trojan。\n"
sub = re.sub(pattern, "@_@", about1)
print(sub)
about2 = "我是一名程序员，我喜欢看计算机网络方面的书，想研究一下开发网站。"
sub = re.sub(pattern, "@_@", about2)
print(sub)
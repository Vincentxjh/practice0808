#第八个练习 - 验证是否出现危险字符

import re
pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
about1 = "我是一名程序员，我喜欢看黑客方面的书，想研究一下Trojan。"
match = re.search(pattern, about1)
if match == None:
    print(about1, "@ 安全！")
else:
    print(about1, "@ 出现了危险词汇！")
about2 = "我是一名程序员，我喜欢看计算机网络方面的书，想研究一下开发网站。"
match = re.search(pattern, about2)
if match == None:
    print(about2, "@ 安全！")
else:
    print(about2, "@ 出现了危险词汇！")
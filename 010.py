#第十个练习 - 输出被@的好友名称（应用正则表达式）

import re
str1 = "@扎克伯格 @俞敏洪 @马云"
pattern = r'\s*@'   #\s表示匹配单个空白符，\s*表示匹配0个或多个空白符
list1 = re.split(pattern, str1)
print("您@的好友有：")
for item in list1:
    if item != "":
        print(item)
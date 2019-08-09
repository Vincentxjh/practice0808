#第三个练习 - 输出被@的好友名称

str1 = "@扎克伯格 @俞敏洪 @库克"
#用空格作为分隔符
list1 = str1.split(' ')
for item in list1:
    print(item)
    print(item[1:])

#用@作为分隔符
list1 = str1.split('@')
for item in list1:
    print(item)

#用空格+@作为分隔符
list1 = str1.split(' @')
for item in list1:
    print(item)
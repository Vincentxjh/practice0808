#第四个练习 - 合并字符串

list_friend = ["扎克伯格", "马云", "俞敏洪", "库克"]
print("您@的好友有： @" + ' @'.join(list_friend))      #由于第一个元素前不加分隔符，所以需自己加上
print("您@的好友有： @", ' @'.join(list_friend))       #对比一下print()函数用逗号和用加号的区别
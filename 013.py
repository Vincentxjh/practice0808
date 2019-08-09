import re
import random
print("----------模拟微信抢红包----------")
money = float(input("请输入要装入红包的总金额（元）："))
t = int(input("请输入红包的个数："))
redpackets_list = []
for i in range(t-1):
    value = round(random.uniform(0,money/2),2)
    money = round((money - value),2)
    redpackets_list.append(value)
redpackets_list.append(money)
for j,k in enumerate(redpackets_list):
    print("第{}个红包：".format(j+1) + "{:.2f}元".format(k))

#第十四个练习 - 显示实时天气预报
import datetime
import random
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
print("{0}年{1}月{2}日\t 天气预报：晴\t 20℃～7℃\t 微风转西风3～4级\n".format(year, month, day))
for i in range(6):
    tempreture = random.randint(7,20)
    j = 8 + i*4
    if j >= 24:
        j = (i-4)*4
    if i == 2 or i == 3:
        print("{:02d}:00\t 天气预报：晴\t {}℃\t 西风3～4级".format(j, tempreture))
    else:
        print("{:02d}:00\t 天气预报：晴\t {}℃\t 微风".format(j, tempreture))
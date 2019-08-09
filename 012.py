#第十二个练习 - 判断车牌归属地

import re
print("第1张车牌号码：")
license_plate1 = "津A·12345"
print(license_plate1)
pattern = r'津A·\d{5}'
match1 = re.match(pattern, license_plate1)
if match1 != None:
    print("这张号牌的归属地：天津")

print("第2张车牌号码：")
license_plate2 = "沪A·23456"
print(license_plate2)
pattern = r'沪A·'
match1 = re.match(pattern, license_plate2)
if match1 != None:
    print("这张号牌的归属地：上海")

print("第3张车牌号码：")
license_plate3 = "京A·34567"
print(license_plate3)
pattern = '[京A·]'
match1 = re.match(pattern, license_plate3)
if match1 != None:
    print("这张号牌的归属地：北京")
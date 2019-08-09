#第七个练习 - 验证输入的手机号码是不是中国移动的号码

import re
pattern = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile1 = "13629845622"
match = re.match(pattern, mobile1)
if match == None:
    print(mobile1, "不是中国移动号码。")
else:
    print(mobile1, "是中国移动的号码。")
mobile2 = "13144222225"
match = re.match(pattern, mobile2)
if match == None:
    print(mobile2, "不是有效的中国移动号码。")
else:
    print(mobile2, "是中国移动的号码。")
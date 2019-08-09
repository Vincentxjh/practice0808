#第二个练习 - 截取字符串

idcard = input("请输入您的身份证号码：")
year = idcard[6:10]
month = idcard[10:12]
day = idcard[12:14]
print("您的生日是" + year + "年" + month + "月" + day + "日。")
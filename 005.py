#第五个练习 - 不区分大小写检验会员名是否存在

#假设已经注册的会员名保存在一个字符串中，用“|”进行分隔
usename_1 = "|MingRi|mr|mingrisoft|WGH|MRSoft|"
usename_2 = usename_1.lower()
regname_1 = input("请输入要注册的会员名称：")
regname_2 = "|" + regname_1.lower() + "|"
if regname_2 in usename_2:
    print("会员名", regname_1, "已经存在！")
else:
    print("会员名", regname_1, "可以注册！")
from random import randint

verify = randint(1000,9999)
print(u"生成的随机数：%d" %verify)

number=input("请输入随机数:")
print(number)
number=int(number)

if number == verify:
    print("登录成功！")
elif number == 132741:
    print("登录成功")
else:
    print("验证码输入有误")
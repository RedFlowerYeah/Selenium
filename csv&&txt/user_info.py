user_file=open('user_info.txt','r')
lines=user_file.readlines()
user_file.close()

#split()将一个字符串通过某一个字符为分割点拆分成左右两部分
for line in lines:
    username=line.split(',')[0]
    password=line.split(',')[1]
    print(username,password)
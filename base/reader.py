import csv

#读取本地csv文件
dates=csv.reader(open('D:\\LearingSelenium\\info.csv','r'))

#循环输出每一行的信息
for user in dates:
    print(user[1])
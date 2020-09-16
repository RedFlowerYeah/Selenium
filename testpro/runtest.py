import unittest

#定义测试用例的目录为当前目录
test_dir = './'
#discover根据当前目录查找测试用例文件，并将查找到的用例组装在测试套件中
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
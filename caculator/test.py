from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    #测试用例初始化的工作
    def setUp(self):
        print("test start")

    def test_add(self):
        #传入要计算的数
        j=Count(2,3)
        #调用unittesst方法进行断言
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117)

    def tearDown(self) :
        print("test end")

        '''
        __name__=="__main"说明被直接调用
        '''
if __name__ == '__main':
    '''
    构造测试集
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))

    '''
    执行测试
    '''
    runner = unittest.TextTestRunner
    runner.run(suite)
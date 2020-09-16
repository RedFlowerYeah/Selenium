from count import is_prime
import unittest

class Test(unittest.TestCase):
    def setUp(self) :
        print("test start")

    def test_case(self):
        self.assertTrue(is_prime(7),msg="Is not prime!")

    def tearDown(self) :
        print("test end")

'''
__name__=="__main"说明被直接调用,main()方法使用TestLoader类来搜索包含以test开头的测试方法并自动执行
'''
if __name__ == "__main":
    unittest.main()
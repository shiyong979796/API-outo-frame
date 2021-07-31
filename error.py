# try:
#     a=int(input("请输入一个整数"))
#     b=int(input('请输入一个整数'))
#     print(a/b)
# except ValueError:
#     print("输入的非整数")
#
# except ZeroDivisionError:
#     print('输入的数不能为0')
#
# except :
#     print('未知错误')


# import unittest
# from parameterized import parameterized
# parmeters=[(1,2,7),(5,2,7),(4,4,9)]
# class my_test(unittest.TestCase):
#
#
#     @parameterized.expand(parmeters)
#     def test11111(self,a, b,c):
#         # print('test 111111')
#         d=a+b
#         self.assertEqual(c,d)
#         print(a,b,c)
#
#     @unittest.skip
#     def testa(self):
#         print('跳过此方法')
#

import unittest
from parameterized import parameterized
class shi(unittest.TestCase):
    @parameterized.expand([(1,2,3,4),(5,6,7,8),("a","b","c","d")])
    def test_111(self,a,b,c,d):
        print(a,b,c,d)
        print(1111)


suite1=unittest.TestSuite()
suite1.addTest(shi("test_01"))

test_runner=unittest.TextTestRunner()
test_runner.run(suite1)


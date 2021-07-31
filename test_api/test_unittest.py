# import unittest
# from parameterized import parameterized #
# class shi(unittest.TestCase):
#     @parameterized.expand([(1, 2, 3, 4,), (5, 6, 7, 8), ("a", "b", "c", "d")])
#     def test_111(self, a, b, c, d):
#         print(a, b, c, d)
#         print(1111)
# suite1=unittest.TestSuite()
# suite1.addTest(unittest.makeSuite(shi))
# test_runner=unittest.TextTestRunner()
# test_runner.run(suite1)


dict1={
    "a":"1",
    "b":"2",
    "c":"3",
    "d":"4",
    "e":"5",
},{
    "a":"11",
    "b":"22",
    "c":"33",
    "d":"44",
    "e":"55",
}
list1=[]
for  i  in  dict1:
    a1=i.get('a')
    b1=i.get('b')
    c1=i.get('c')
    d1=i.get('d')
    e1=i.get('e')
    list1.append((a1,b1,c1,d1,e1))
    print('list1={}'.format((a1,b1,c1,d1,e1)))

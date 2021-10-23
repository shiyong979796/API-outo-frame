#导包
from config import base_dir #导入赋值好的路径 类属性
import time
import unittest
# from  scripst.Test01_login import Test_login
from tools.HTMLTestRunner import HTMLTestRunner


#封装测试套件
#方案1
# suite=unittest.TestSuite()#封装测试套件
# suite.addTest(unittest.makeSuite(Test_login))  #把整个类的 test方法  放进套件中
#
#方案2
#
suite=unittest.TestLoader().discover(base_dir,'test*.py')  #运行指定路径下以test02开头 内的所有test方法

#指定测试报告路径
report="./report/{}.HTML".format(time.strftime("%Y%m%d-%H%M%S")) #指定测试报告路径与文件名称

#文件流形式打来文件
with open(report,"wb")as f:   #打开文件 open方法 传入 路径，wb  写 二进制
    #创建HTMLTesm tRunner运行器
    runner = HTMLTestRunner(f,title="tpshop接口测试报告") #HTMLTestRunner 运行器，传入报告路径 ，与title
    #执行测试套件
    runner.run(suite)          #运行测,,,,,,,,,,,,,,,,,,,,,,,,,试套件
    
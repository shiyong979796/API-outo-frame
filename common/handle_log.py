#:@ TIME 2021/10/23   22:04
#:@FILE  handle_log.py
#:@EMAIL  1557225637@QQ.COM
import logging
import path
import time
from common.handle_cf_file import new_cfFile
cf=new_cfFile
class Loggingg(logging.Logger):
    '''
    1.创建Loggingg(logging.Logger)类 继承logger
        2.属性初始化 （name，lever，file=None，format，）
        3.supre()重新父类属性
    # 创建收集器
    #创建控制台渠道
    #设置格式
    #渠道绑定格式
    #收集器绑定渠道
    '''

    def  __init__(self,
                  name=cf.get_str('Log','name'),
                  lever=cf.get_str('Log','level'),
                  file=cf.get_str('Log','file_ok'),
                  fmt='%(asctime)s:%(name)s:%(funcName)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s'
                  ):
        super().__init__(name,lever)

        # 创建收集器
        logger = logging.getLogger(name)
        #设置收集器级别
        logger.setLevel(logging.DEBUG)
        #创建控制台渠道
        concel_handel=logging.StreamHandler()
        #设置格式
        formats=logging.Formatter(fmt)
        #渠道绑定格式
        concel_handel.setFormatter(formats)
        #收集器绑定渠道
        self.addHandler(concel_handel)

        if file:
            # 创建文件渠道
            # file_handel = logging.FileHandler(path.log_dir + r'\{}.log'.format(time.strftime("%Y%m%d-%H%M%S")), mode='w', encoding='utf-8')
            file_handel = logging.FileHandler(path.log_dir + r'\{}.log'.format('new_log'), mode='w', encoding='utf-8')
            file_handel.setLevel(lever)
            file_handel.setFormatter(formats)
            self.addHandler(file_handel)
new_log=Loggingg()
#name='log',file=config.log_dir+r'\new_log.txt'
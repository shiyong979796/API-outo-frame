#:@ TIME 2021/10/23   22:06
#:@FILE  handle_cf_file.py
#:@EMAIL  1557225637@QQ.COM
import os
from configparser import ConfigParser
import path
class Config_file:
    '''
    1.from configparser import ConfigParser
    2.创建 Config_file类
        属性初始化（file_path）
        创建ConfigParser()对象
        用对象 read方法读取文件
    3.创建方法
        get_str
        get_bool
        get_float
        get_int
    '''
    def __init__(self,file_path):
        self.new_config_parser=ConfigParser()
        self.red_file=self.new_config_parser.read(file_path,'utf-8')

    def get_str(self,section,option):
        return self.new_config_parser.get(section,option)

    def get_bool(self,section,option):
        return self.new_config_parser.getboolean(section,option)

    def get_float(self,section,option):
        return self.new_config_parser.getfloat(section,option)

    def get_int(self,section,option):
        return self.new_config_parser.getint(section,option)


file=os.path.join(path.config_file_dir, 'config_file.ini')
new_cfFile=Config_file(file)








'''
继承configparser  只需要重写下路径

class Config_file(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")



file_path = os.path.join(config.config_file_dir,'config_file.ini')
new_cfFile = HandleConfig(file_path)


'''



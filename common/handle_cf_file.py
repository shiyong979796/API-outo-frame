#:@ TIME 2021/10/23   22:06
#:@FILE  handle_cf_file.py
#:@EMAIL  1557225637@QQ.COM

from configparser import ConfigParser
import config
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

new_cfFile=Config_file(config.conifg_file_dir)
print(new_cfFile.get_str('Log','name'))

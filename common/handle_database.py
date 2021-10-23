#:@ TIME 2021/10/23   22:04
#:@FILE  handle_database.py
#:@EMAIL  1557225637@QQ.COM
import pymysql

class Database:
    '''
    1.创建Database类
        2.数据初始化 连结属性 pymysql.connect(（host，port，user,password,database,charset）
        3.获取游标 cursor 返回字典数据：self.connect.cursor(pymysql.cursors.DictCursor)
        4.定义 方法
         传入sq，执行sq
         返回 游标.fachall、one 数据
         返回影响行数
         刷新数据 connect.commit（）
    '''

    #创建连结
    # def __init__(self,host,port,user,password,database):
    #     self.connect=pymysql.connect(
    #         host=host,
    #         port=port,
    #         user=user,
    #         password=password,
    #         database=database,
    #         charset='utf8',
    #     )
    def __init__(self):
        self.connect=pymysql.connect(
            host='rm-uf60nj0t33i3601vx3o.mysql.rds.aliyuncs.com',
            port=3306,
            user='root',
            password='shi1557225637_',
            database='table_one',
            charset='utf8',

        )
        #获取游标
        self.cur=self.connect.cursor(pymysql.cursors.DictCursor)

    def get_fetchall(self,sq):
        self.cur.execute(sq)
        return self.cur.fetchall()

    def get_fetchone(self,sq):
        self.cur.execute(sq)
        return self.cur.fetchone()

    def count_line(self,sq):
        count=self.cur.execute(sq)
        return count

    def commit(self):
        self.connect.commit()
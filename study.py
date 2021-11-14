#:@ TIME 2021/11/6   16:11
#:@FILE  study.py
#:@EMAIL  1557225637@QQ.COM

print('n:名词')
print('adj:形容词')
print('vt：动词')
print('adv:复词')
def study(dict_word,dict_dont_word,dict_too_easy,):
    while True:
        dict_failed = {}
        try:
            res=int(input('输入学习方式：0：复习不会的，1：复习会的，2：复习简单的，3：复习 1和2,4：结束本单元：'))
            if res==4:
                break
            way=int(input('请输入学习方式：1：看中 写英，2：看英语 like 中:'))
        except:
            print('wrong format 、please retype must int  ')
            continue
        if res == 0:
            if way == 1:
                for  key,value in dict_dont_word.items() :
                    enter=input('请输入：（{}）的英文翻译:'.format(key))
                    if enter == value:
                        print('输入正确：{}:{}'.format(key,value))
                    elif enter =='3':
                        break
                    else:
                        print('输入错误：正确的（{}）:输入的（{}）'.format(value,enter))
                        dict_failed[key]=value
                study_failed(dict_failed)
            else:
                for key,value in dict_dont_word.items():
                    enter=input('请输入：（{}）的中文翻译：'.format(value))
                    if enter in key:
                        print('输入正确：{}:{}'.format(key,value))
                    elif enter =='3':
                        break
                    else:
                        print('输入错误：正确的（{}）:输入的（{}）'.format(key,enter))
                study_failed(dict_failed)



        elif res ==1:
                if way == 1:
                    for key, value in dict_word.items():
                        enter = input('请输入：（{}）的英文翻译：'.format(key))
                        if enter == value:
                            print('输入正确：{}:{}'.format(key, value))
                        elif enter == '3':
                            break
                        else:
                            print('输入错误：正确的（{}）:输入的（{}）'.format(value, enter))
                    study_failed(dict_failed)
                else:
                    for key,value in dict_word.items():
                        enter = input('请输入：（{}）的中文翻译：'.format(value))
                        if enter in key:
                            print('输入正确：{}:{}'.format(key, value))
                        elif enter == '3':
                            break
                        else:
                            print('输入错误：正确的（{}）:输入的（{}）'.format(key, enter))
                    study_failed(dict_failed)


        elif res ==2:
                if way == 1:
                    for key, value in dict_too_easy.items():
                        enter = input('请输入：（{}）的英文翻译：'.format(key))
                        if enter == value:
                            print('输入正确：{}:{}'.format(key, value))
                        elif enter == '3':
                            break
                        else:
                            print('输入错误：正确的（{}）:输入的（{}）'.format(value, enter))
                    study_failed(dict_failed)
                else:
                    for key, value in dict_too_easy.items():
                        enter = input('请输入：（{}）的中文翻译：'.format(value))
                        if enter in key:
                            print('输入正确：{}:{}'.format(key, value))
                        elif enter == '3':
                            break
                        else:
                            print('输入错误：正确的（{}）:输入的（{}）'.format(key, enter))
                    study_failed(dict_failed)
        elif res ==3:
            dict_word.update(dict_dont_word)
            if way == 1:
                for key, value in dict_word.items():
                    enter = input('请输入：（{}）的英文翻译：'.format(key))
                    if enter == value:
                        print('输入正确：{}:{}'.format(key, value))
                    elif enter == '3':
                        break
                    else:
                        print('输入错误：正确的（{}）:输入的（{}）'.format(value, enter))
                study_failed(dict_failed)

            else:
                for key, value in dict_word.items():
                    enter = input('请输入：（{}）的中文翻译：'.format(value))
                    if enter in key:
                        print('输入正确：{}:{}'.format(key, value))
                    elif enter == '3':
                        break
                    else:
                        print('输入错误：正确的（{}）:输入的（{}）'.format(key, enter))
                study_failed(dict_failed)
        elif res==4:
            print('skip unit')
            break
def study_failed(dict_failed):
    while True:
        try:
            res = int(input('本次测试错误的有:{},是复习错误的？0 or 1'.format(dict_failed)))
        except:
            print('data type must int')
            continue
        if res == 1:
            for key, value in dict_failed.items():
                enter = input('请输入：（{}）的英文翻译:'.format(key))
                if enter == value:
                    print('输入正确：{}:{}'.format(key, value))
                elif enter == '3':
                    break
                else:
                    print('输入错误：正确的（{}）:输入的（{}）'.format(value, enter))
                    dict_failed[key] = value
        else:
            break
def read_word():
    list_words=[]
    list_dont_word=[]
    list_too_easy=[]

    dict_word={}
    dict_dont_word={}
    dict_too_easy={}
    print('n:名词')
    print('adj:形容词')
    print('vt：动词')
    print('adv:复词')

    while True :
        try:
            word1=int(input('will be：？'))
        except:
            print('Wrong format，please retype,must int')
            continue
        #会
        if word1==1:
            word = input('please  enter  word：')
            china=input('please enter  chinese：')
            list_words.append(word)
            dict_word[china]=word
        #不会
        elif word1==0:
            word=input('please enter dont work：')
            china = input('please enter  chinese：')
            list_dont_word.append(word)
            dict_dont_word[china]=word
        #简单
        elif word1==2:
             word=input('please enter  easy work：')
             china = input('please enter  chinese：')
             list_too_easy.append(word)
             dict_too_easy[china]=word
        #跳出
        elif word1 ==3:
             break
        #重新输入
        else:
            continue

    print('list_words：',list_words)
    print('dont_work：',dict_dont_word)
    print('too  easy  work：',list_too_easy)
    print('dict_work：',dict_word)
    print('dict_dont_word：',dict_dont_word)
    print('dict_too_easy：',dict_too_easy)

def one_on():
    # 会
    dict_word = {'那里，在那里，到那里': 'there ', '八': 'eight', '猴子': 'monkey', '绿色': 'green', '拥有，得到，吃，喝，进行，从事': 'have',
                 '许多的': 'many', '老虎': 'tiger', '橙子，橙色的': 'orange', '七': 'seven', '鼻子': 'nose', '眼睛': 'eyes ',
                 '嘴': 'mouth', '九': 'nine', '是 ，（系动词，be的人称形式之一）': 'are', '鸟': 'bird', '喜欢，像，如同': 'like', '书': 'book',
                 '做，干，做什么': 'do'}

    # 不会
    dict_dont_word = {'梨': 'pear', '铅笔': 'pencil', '颜色，给。。。。涂色': 'colour', '嘴，口': 'mouth'}

    # 简单
    dict_too_easy = {'尺子，管理者': 'ruler', '黑色，黑色的': 'black', '耳朵': 'ear', '这，这个，这是': 'this', '它': 'it', '什么': 'what',
                     '不，不是': 'no', '黄色的': 'yellow', '三，三个': 'three', '脸': 'face', '猫': 'cat', '一': 'one',
                     '是（be的第三人称单数形式）': 'is', '狗': 'dog', '多少，如何': 'how', '老师，教师': 'teacher', '蓝色': 'blue', '红色': 'red',
                     '我': 'i', '苹果': 'apple', '一个': 'a', '香蕉': 'banbana', '六': 'six', '二': 'two', '四': 'four',
                     '五': 'five', '我的': 'my', '是 是的': 'yes', '十': 'ten', '你': 'you'}

    study(dict_word,dict_dont_word,dict_too_easy)
def one_under():
    dict_word={'牛奶': 'milk', '黑板': 'blackboard', '服装，连衣裙': 'dress', '短裤': 'shorts', '光，光线': 'light',
                '果汁，菜汁，饮料': 'juice', '蔬菜': 'vegetable', '鸡肉，小鸡': 'chicken', '附近': 'near', '衬衫': 'shirt',
                'T恤': 't-shirt', '书桌': 'desk', '门': 'door', '椅子': 'chair', '0': 'sure', '汽车，小汽车': 'car', '你的，你们的': 'your'}

    dict_dont_word={'口渴，渴望的': 'thirsty', '鱼': 'fish', '饿了': 'hungry', '在。。之后': 'behind', '熊': 'bear',
                     '飞机': 'plane', '在。。下面': 'under'}


    dict_too_easy= {'盒子，箱子': 'box', '在。。': 'in', '蛋': 'egg', '火车': 'train', '和': 'and', '水，给。。。喝水': 'water',
                    '对不起，抱歉': 'sorry', '米饭，大米': 'rice', '可能，可以': 'can', '在。。上': 'on', '这，独一无二的 指': 'the', '床': 'bed',
                    '需要，想要': 'want', '茶': 'tea', '裙子': 'skirt'}

    study(dict_word,dict_dont_word,dict_too_easy)


def two_on():
    dict_word={'姐，妹': 'sister', '高的': 'tall', '花': 'flower', '高兴，愉快的': 'happy', '也，还，又，过分，非常': 'too', '他的': 'her',
                '草地': 'grass', '兄弟': 'brother', '超级市场，超市': 'supermarket', '祖母，外祖母': 'grandmother', '书店': 'bookshop',
                '动物园': 'zoo', '树': 'tree', '小山': 'haill', '0': 'handsome', '帅气的': 'handsome', '这儿，这里': 'here',
                '卡片，纸牌': 'card', '朋友': 'firend', '女人，妇女': 'woman', '男人': 'man'}
    dict_dont_word={'高兴的，愉快的': 'mearry', '做，工作，有用': 'does', 'n.礼物': 'present', '湖': 'lake', '大的': 'big',
                     '同班同学': 'classmate', '漂亮的 形容美丽的': 'pretty', '医院': 'hospital', '他的 ': 'his', '船': 'boat',
                     '瘦的': 'thin', '瘦的，单薄的': 'thin', 'for': '（表示对象）给，（表示目的）为，（表示去向）往，向',
                     '（表示对象）给，（表示目的）为，（表示目标，去向）往': 'for'}
    dict_too_easy={'名字': 'name', '他': 'he', '她': 'she', '到，往，去做，达到': 'to', '或者': 'or', '谁': 'who', '父亲': 'father',
                    '母亲': 'mother', '女孩': 'girl', '谢谢，感谢': 'thank', '学校': 'school', '男孩': 'boy', '新年': 'new year',
                    '看，看上去，敲上去': 'look', '新的': 'new'}

    '''
    请输入：（高兴的，愉快的）的英文翻译:pretty
    输入错误：正确的（mearry）:输入的（pretty）

    请输入：（医院）的英文翻译:	pital
    输入错误：正确的（hospital）:输入的（	pital）

    请输入：（船）的英文翻译:toke
    输入错误：正确的（boat）:输入的（toke）

    '''

    study(dict_word,dict_dont_word,dict_too_easy)
def two_under():
    print('study_two_under')
    dict_word={'踢足球，对于难办的事情踢足球': 'playfootball、', '冷的，失去感觉': 'cold', '十二': 'twelve', '什么时候，当时，什么情况下': 'when',
                '凉爽的，形容酷': 'cool', '哇偶，称赞': 'wow', '春季，温泉': 'spring', '骑自行车': 'ride bike', '温暖的': 'warm',
                '每天': 'every day'}
    dict_dont_word= {'特别喜爱的，中意的': 'favourite', 'windy': 'winday', '多风，风大的': 'windy', '多雨，下雨': 'rainy', '二十': 'twenty',
                     '周六': 'Saturday', '伞，形容保护伞': 'umbrella', '吃早餐': 'eat breakfast', '0': 'eat breakfast',
                     '十五': 'fifteen', '十四': 'fourteen', '冬天，冬季': 'winter', '星期四': 'thursday', '多雪的，雪白的': 'snowy',
                     '季节': 'season', '十三': 'thirteen', '朝，向，在，某处': 'at', '夏季': 'summer', '周日': 'sunday',
                     '阳光明媚的': 'sunny', '星期五': 'friday', '秋季，秋天': 'autumn', '天气': 'weather', '星期三': 'wednesday',
                     '星期二': 'tuesday'}
    dict_too_easy= {'热的，辣的': 'hot', '今天，现在': 'today', '十一': 'eleven', '游泳': 'swim', '去学校': 'go to school',
                    '去睡觉': 'go to bed', '让我们': 'let’s', '不能': 'can‘t', '玩游戏': 'playtime', '回家': 'go home', '时间': 'time'}

    study(dict_word,dict_dont_word,dict_too_easy)

def three_on():
    print('study_three_on')
    dict_word= {'星期，周': 'week', '应该，能，过去式 ！': 'should', '长的': 'long', '第一': 'first'}
    dict_dont_word= {'土豆，马铃薯': 'potato', '亲爱的，可爱的': 'dear', '水果': 'fruit', '手臂': 'arm', '年纪，等级，评分': 'grade',
                     '龟，海龟': 'turtle', '坏的，严重的 ，形容心情，事务，人': 'bad', '厚衫，毛衣': 'sweater', '四月': 'april', '宠物': 'pet',
                     '裤子，长裤': 'trousers'}
    dict_too_easy= {'老虎': 'tiger', '参数，身体，正文': 'body', '聚会，党派': 'party', '0': 'shopping list', '十二月': 'december'}

    study(dict_word,dict_dont_word,dict_too_easy)
def three_under():
    dict_word= {'一起玩': 'play with', '浴间': 'bathroom', '多的，大量的': 'much', '操场': 'playground', '们': 'door',
                '客厅': 'living room', '他们': 'they', '跳舞': 'dance', '餐厅': 'dining room', '那，那个': 'that', '我们的': 'our',
                '家人 ': 'family', '游泳': 'swim', '叔叔': 'uncle', '中国的 ，中国人': 'chinese', '每人': 'everyone', '音乐': 'music',
                '跑，管理': 'run', '英语': 'egnlish'}
    dict_dont_word={'漂亮，美丽的': 'beautiful', '出租，rent出租': 'for rent', '孩子': 'children', '第二': 'second', '厨房': 'kitchen',
                     '': '', '厕所': 'toilet', '科学': 'science', '数学': 'maths', '表弟，表兄': 'cousin', '阿姨，伯母，姑，婶': 'aunt ',
                     '丢失了 ，迷路了': 'lost', '非常，真正的': 'really', '图书馆': 'library', '艺术': 'art', '体育': 'pe', '第三': 'third',
                     '明天': 'tomorrow', '欢迎': 'welcome', '地板，地面': 'floor', '水瓶，水浒': 'water bottle'}
    dict_too_easy={'学习，研究，书房': 'study', '放学后': 'after school', '我们': 'we', '房价': 'room', '光，灯': 'light', '沙发': 'sofa',
                    '知道，懂': 'know', '家': 'home', '唤醒': 'wake up', '1': 'bedroom', '好，可以': 'ok', '班级，教室': 'classroom'}


    study(dict_word,dict_dont_word,dict_too_easy)

# read_word()
# three_under()
three_on()
three_under()
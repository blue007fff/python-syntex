# 파이썬 기본 문법 정리

class subject_printer:
    def __init__(self, function):
        print(f'{"":{"="}<{50}}')
        print(f'{function.__name__ :{"="}<{50}}')   
        print(f'{"":{"="}<{50}}')

    def __del__(self):        
        print(f'{"":{"_"}<{50}}')
        print("")

def mysyntex_test_sys():
    subject = subject_printer(mysyntex_test_sys)
    import os
    import sys    
    
    print (os.path.dirname(sys.executable) + '\Scripts\\')
    print(sys.version)

def mysyntex_test_print():    
    subject = subject_printer(mysyntex_test_print)
    print('pi = ', 3.141592)

    # end : 줄바꿈 문자 대신 다른 문자 사용 가능.
    print('pi = ', end='')
    print(3.141592)

    print('pi ', end="===")
    print(3.141592)

    print(1920, 1080, sep=' x ')    # sep에 x를 지정

    # format
    print("{0} {1} {2}".format('first', 'second', 'third'))
    print("{0} {1} {2}".format('pi', '=', 3.14))    
    print("{0:5d} {1} {2:.3f}".format(314, ',', 3.141592))
    print(f"{314:05d} {','} {3.141592:.3f}")
        
    print(f'{"padding":{"="}<{30}}')
    print(f'{"padding":{"="}>{30}}')
    print(f'{"padding":{"="}^{30}}')

    print(f'{"first":{"!"}<{10}} {"second"} {"third"}')

    print('{:<15}'.format('padding'))
    print('{:>15}'.format('padding'))
    print('%15s' % ('padding'))
    print('%-15s' % ('padding'))

    # 숫자 입력 //readline이 더 빠르다고 배움
    #a, b = map(int,list(sys.stdin.readline().split()))


def mysyntex_test_type():
    subject = subject_printer(mysyntex_test_type)
    print(type(None))
    print(type(314))
    print(type(3.14))
    print(type("3.14"))
    print(type(True))
    print(type([1, 2, 3]))
    print(type((1, 2, "3")))
    tuple_a = 1, 3
    print(type(tuple_a), tuple_a)
    print(type({1:"first", 2:"second", 3:"third"}))

    class myclass():
        m_a = 0
    print(type(myclass()))

    # casting    
    a = "3.14"
    print(a)
    a = float(a)
    print("float(a)", a)
    a = int(a * 100)
    print("int(a)", a)
    a = str(a)
    print("str(a)", a)

    a = list(range(5))
    print(type(a), a)
    a = tuple(a)
    print(type(a), a)
    a = set(a)
    print(type(a), a)
    a = list(a)    
    print(type(a), a)

def mysyntex_test_branch():
    subject = subject_printer(mysyntex_test_branch)

    while 1:
        score = int(input("Enter score (0~100) : "))
        if (0 <= score and score <= 100):  # and/or
            if (score == 100):
                print("S : ", score)
            elif (score >= 90):
                print("A : ", score)
            elif (score >= 80):
                print("B : ", score)
            else:
                print("F : ", score)
        else:
            break
    print("end")

    a_list = list(range(10))
    while 1:
        a = int(input("Enter  : "))
        if a in a_list:
            print('a is in ', a_list)
        else:
            break


def mysyntex_test_loop():
    subject = subject_printer(mysyntex_test_loop)

    # for loop
    print("for i in range(1, 10) :", end=' ')
    for i in range(1, 10):
        print(i, end=' ')
    print()

    print("for i in range(1, 10, 3) :", end=' ')
    for i in range(1, 10, 3):
        print(i, end=' ')
    print()

    print("for i in \"Hello world\" :", end=' ')
    for i in "Hello world":
        print(i, end=' ')
    print()

    a_list = list(range(10))
    for i in a_list:
        print(i, end=' ')
    print()

    inputstring = ""
    while inputstring != "exit":
        inputstring = input("Input : ")
        print(inputstring)
    print("exit while")


def mysyntex_test_class():
    subject = subject_printer(mysyntex_test_class)
    class myclass():
        m_a = 0
        
        def __init__(self, m_b, m_c):
            self.m_b = m_b
            self.m_c = m_c

        def print_type(self):
            print(type(self))
            print("m_a : ", type(self.m_a))
            print("m_b : ", type(self.m_b))
            print("m_c : ", type(self.m_c))

    # class 멤버도 중간에 타입 변경이 가능하네...
    myclass_var = myclass(314, "3.14")
    myclass_var.print_type()
    myclass_var = myclass(3.14, "3.14")
    myclass_var.print_type()


def mysyntex_test_list():
    subject = subject_printer(mysyntex_test_list)

    a_list = list(range(10))
    print("a_list :", a_list)

    a_list = list(range(2, 10, 3))
    print("a_list :", a_list)   

    a_list = list(range(10))
    a_list = [2*x+1 for x in a_list]
    print("a_list :", a_list)
    
    a_list = list(range(10))
    a_list = [2*x for x in a_list if x < 5]
    print("a_list :", a_list)

    # num_list = [423, 234, 3534, 6765, 123]
    # print("num_list : ", num_list)
    # print("num_list[1:4] : ", num_list[1:4])
    # num_list.insert(2, 333)
    # num_list.remove(123)
    # num_list.append(999)
    # print("num_list : ", num_list)

    # mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # print("mat :", mat)
    # mat[2].append(1)
    # print("mat :", mat)

def mysyntex_test_tuple():
    subject = subject_printer(mysyntex_test_tuple)

    num_tuple = ("one", "two", "three", "four")
    print("num_tuple : ", num_tuple)
    print("two idx : ", num_tuple.index("two"))
    print("num_tuple[3] : ", num_tuple[3])

def mysyntex_test_dict():
    subject = subject_printer(mysyntex_test_dict)

    num_dic = {1:"one", 2:"two", 3:"three"}
    print("num_dic[1] : ", num_dic[1])

def mysyntex_test_string():
    subject = subject_printer(mysyntex_test_string)

    string = """줄바꿈 가능
    줄바꿈 가능
    줄바꿈 가능"""
    print(string)
    print("string len : ", len(string))

    string = "test test"
    print(string)
    string = string.upper()
    print("upper : ", string)
    string = string.lower()
    print("lower : ", string)
    string = string.capitalize()
    print("capitalize : ", string)
    string = string.title()
    print("title : ", string)
    string = string.split(" ")
    print("split : ", string)
    string = " test test "
    string = string.strip(" ")
    print("strip : ", string)
    print("Hello world"[7:10])
    print("일이삼사오육칠팔구십"[7:10])

from array import*
def mysyntex_test_array():
    subject = subject_printer(mysyntex_test_array)
    num_array = array('i', [43, 523, 432, 5235,67])
    print("num_array : ", num_array)
    sorted(num_array)
    num_array.pop()
    num_array.append(343)
    num_array.reverse()


import csv
def mysyntex_test_fileio():
    subject = subject_printer(mysyntex_test_fileio)
    # write/read text
    file = open("test.txt", "w")
    file.write("one-")
    file.write("two-")
    file.write("three-")
    file.close()

    file = open("test.txt", "r")
    print(file.read())
    file.close()

    #cvs
    file = open("test.csv", "w")
    record = "one, two, three\n"
    file.write(str(record))
    record = "one, two\n"
    file.write(str(record))
    file.write(str(record))
    file.close()

    print("file = open(\"test.csv\", \"r\")")
    file = open("test.csv", "r")
    for row in file:
        print(row)
    file.close()

    file = open("test.csv", "r")
    reader = csv.reader(file)    
    print(reader)

    rows = list(reader)
    for i in rows:
        print(i)
    
    print(len(rows))
    for i in range(0, len(rows)):
       print("rows[{0}] :".format(i), rows[i])


def mysyntex_test_fileio_encoding():
    subject = subject_printer(mysyntex_test_fileio_encoding)

    with open("test_cp949.txt", 'w', encoding='cp949') as f:
        f.write("one, two, three\n")
        f.write("하나, 둘, 셋")

    with open("test_utf8.txt", 'w', encoding='utf-8') as f:
        f.write("one, two, three\n")
        f.write("하나, 둘, 셋")

    lines = []
    data = ''
    with open("test_cp949.txt", 'r', encoding='cp949') as f:
        #lines = f.readlines()
        data = f.read()

    # for line in lines:
    #     print(line)
    print(data)

    # encode 형식이 다르면 예외 처리 됨.
    #with open("test_cp949.txt", 'r', encoding='utf-8') as f:
    with open("test_utf8.txt", 'r', encoding='utf-8') as f:
        #data = f.read()
        lines = f.readlines()

    for line in lines:
        print(line, end='')
    print()
    #print(data)


def mysyntex_test_fileio_json():
    subject = subject_printer(mysyntex_test_fileio_json)

    import json

    #JSON              파이썬
    #오브젝트(object)   dict
    #배열(array)        list
    #문자열(string)     str
    #숫자 (정수)        int
    #숫자 (실수)        float
    #true              True
    #false             False
    #null              None

    # 원소 끝부분에 ',' 들어가면 안됨
    json_string = '''{
        "apple": "사과",
        "banana": "바나나",
        "Group": {
            "One": 1,
            "Two": 2
        },
        "True": true,
        "Null": null,
        "리스트": ["one", "two", "three"]
    }
    '''
    json_object = json.loads(json_string)
    print(f'json_object : {type(json_object)}')

    assert json_object['apple'] == "사과"
    assert json_object['banana'] == '바나나'
    assert json_object['Group']['One'] == 1
    assert json_object['True'] is True
    assert json_object['Null'] is None
    assert isinstance(json_object['리스트'], list)

    json_string = json.dumps(json_object)
    print(json_string)
    json_string = json.dumps(json_object, indent=2)
    print(json_string)

    with open("test.json", "w") as f:
        #f.write(json_string)
        json.dump(json_object, f, indent=2)

    with open("test.json", "r") as f:
        json_string = f.read()
    print(json_string)

    json_object = json.loads(json_string)
    print(json_object)
    print(f'json_object : {type(json_object)}')

    with open("test.json", "r") as f:
        json_object = json.load(f)
    print(f'json_object : {type(json_object)}')
    print(json_object)
    



#import 모듈명
#from import 모듈명 변수/함수/클래스
#from import 모듈명 *
#import 모듈명 as 별명
#from import 모듈명 변수/함수/클래스 as 별명
def mysyntex_test_module():
    subject = subject_printer(mysyntex_test_module)

from pathlib import Path
def mysyntex_test_module_pathlib():
    subject = subject_printer(mysyntex_test_module_pathlib)

    print(Path.cwd())
    print(Path.home())
    
    relpath = Path("test.txt") 
    print(relpath)
    relpath = relpath.resolve() #현재 디렉토리를 기준으로 절대경로로 변경.
    print(relpath)

    rel_dir = Path('.')
    pal_rel_dir = Path('..') #Path('./..')

    print(f'{"":{"-"}<{30}}')

    filepath = Path("C:\\Users\\SeongJu\\Desktop\\python-syntex\\test.txt")  
    print(filepath)
    print(filepath.parent)
    print(filepath.name)
    print(filepath.stem)
    print(filepath.suffix)    
    print(f'{"":{"-"}<{30}}')

    print(filepath.exists())
    print(filepath.is_dir())
    print(filepath.is_file())
    print(filepath.home())

    print(f'{"":{"-"}<{30}}')
    dirpath = rel_dir = Path('.')
    print(dirpath.mkdir('Test/A'), True)
    print(dirpath.mkdir('Test/B'))
    #print(filepath.touch())
    #print(filepath.unlink())
    #print(dirpath.rmdir())

from datetime import date, time, datetime, timedelta
def mysyntex_test_module_datetime():
    subject = subject_printer(mysyntex_test_module_datetime)

    date_obj= date(2020, 10, 3)    
    time_obj = time(15, 23, 21)
    datetime_obj = datetime(2022, 12, 11, 7, 30, 25)

    print(date_obj)
    print(time_obj)
    print(datetime_obj)

    date_obj2= date(2020, 8, 3)
    diff_date = date_obj2 - date_obj
    print(type(diff_date),  diff_date)

    today = date.today()
    now = datetime.now()
    print(today, now, sep=' : ')

import locale
def mysyntex_test_module_locale():
    subject = subject_printer(mysyntex_test_module_locale)

    now = datetime.now()
    locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
    print(locale.getlocale())
    print("{0:%A}, {0:%a}".format(now))
    print("{0:%B}, {0:%b}".format(now))    
    print(now.strftime("%Y-%m-%d:%A : %H:%M:%S(%p)"))
    print(f'{"":{"-"}<{30}}')

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    print(locale.getlocale())
    print("{0:%A}, {0:%a}".format(now))
    print("{0:%B}, {0:%b}".format(now))
    print(now.strftime("%Y-%m-%d:%A : %H:%M:%S(%p)"))


def mysyntex_test_numpy():
    subject = subject_printer(mysyntex_test_numpy)

    import numpy as np

    arr = np.array([0, 1, 2, 3, 4, 5])
    print(type(arr), arr)

    arr = np.array([0, 1, 2, 3, 4, 5], dtype=np.uint)
    arr = np.array([0, 1, 2, 3, 4, 5], dtype=np.float32)
    arr = arr.astype(np.int)

    arr2 = np.array([[1,0,0], [0,1,0], [0,0,1]])
    print(arr2)

    print(type(arr.shape), arr.shape)
    print(type(arr2.shape), arr2.shape)

    arr3 = np.array(["one", "two", "three"])
    print(arr3)
    print(arr3.dtype)

    arr = np.arange(0, 10, 1)
    print("np.arange(0, 10, 1) : ", arr)

    arr = np.linspace(1, 10, 8)
    print("np.linspace(1, 10, 8) : ", arr)  

    print(f'{"reshape":{"-"}<{30}}')
    arr = np.arange(0, 8, 1)
    print('np.arange(0, 8, 1)', arr.shape)
    print(arr)
    arr = arr.reshape(2, 4)
    print('arr.reshape(2, 4)', arr.shape)
    print(arr)
    arr_8 = arr.reshape(8,)
    arr_8x1 = arr.reshape(8, 1) # 2차원 배열임
    print('arr_8', arr_8.shape)
    print(arr_8)
    print('arr_8x1', arr_8x1.shape)
    print(arr_8x1)
    #arr = arr.reshape(3, 3) # exception
    
    arr = np.arange(1, 11, 1)    
    print('sum, mean', arr.sum(), arr.mean())
    print('std, var', arr.std(), arr.var())
    print('min, max', arr.min(), arr.max())
    print('cumsum', arr.cumsum())
    print('cumprod', arr.cumprod())


    arr = np.arange(0, 10, 1)
    arr2 = arr[1:4]
    print(arr2)
    arr2 = arr[1:4:2]
    print(arr2)
    arr2 = arr[8:2:-2]
    print(arr2)
    arr2 = arr[::-1]
    print(arr2)
    arr2 = arr[[3, 6, 9, -1]]
    print(arr2)
    arr2 = arr[((arr%2)==0) & (arr > 5)]
    print(arr2)
    arr2 = arr[((arr%2)==0) | (arr > 5)]
    print(arr2)

    arr[5:] = 10
    print(arr)
    

import numpy as np
import pandas as pd
def mysyntex_test_pandas():
    subject = subject_printer(mysyntex_test_pandas)

    s1 = pd.Series(list(range(0, 10, 2)))
    print(type(s1))
    print(s1)
    print(s1.index)
    print(s1.values)

    index_data = ['2022-12-18', '2022-12-19', '2022-12-20']
    data = [3500, 3600, np.nan]
    s1 = pd.Series(data, index = index_data)
    print(s1)

    s1 = pd.Series({'One':1, 'Two':2, 'Three':3})
    print(s1)

    index_data = pd.date_range(start='2020-02-27', end='2020-03-01')
    data = [3500, 3579, np.nan, 3782]
    s1 = pd.Series(data, index = index_data)
    print(s1)

    dates = pd.date_range(start='2020-02-27', end='2020-03-30', freq='2D')
    print(dates)

    dates = pd.date_range(start='2020-02-27', periods=12)
    print(dates)

    dates = pd.date_range(start='2020-02-27', periods=12, freq='B') #업무일(월~금) 기준
    print(dates)

    dates = pd.date_range(start='2020-02-27 10:00', periods=5, freq='30min')
    print(dates)

    s1 = pd.Series({'B':4.0, 'A':5.0, 'C':3.0, 'D':1.0})
    print(s1)
    s1 =s1.reindex(['A', 'B', 'C', 'D', 'E'])
    print(s1)

def mysyntex_test_pandas_dataframe():
    subject = subject_printer(mysyntex_test_pandas_dataframe)

    data = [[1,2,3], [4,5,6], [7,8,9]]
    df = pd.DataFrame(data)
    print(type(df))
    print(df)

    data = np.arange(1, 13, 1).reshape(4, 3)
    index_data = pd.date_range('2020-01-11', periods=4)
    columns_data = ["A", "B", "C"]
    df = pd.DataFrame(data, index=index_data, columns=columns_data)
    print(df)

    dict_data = {
        '연도' : [2017, 2017, 2018, 2018, 2019, 2019], 
        '지사' : ['한국', '미국', '한국', '미국', '한국', '미국'], 
        '고객수' : [200, np.nan, 250, 450, 300, 500], 
    }
    df = pd.DataFrame(dict_data)
    print(df)
    print(df.index)
    print(df.columns)
    print(df.values)

    df1 = df.set_index('연도')
    print(df1)

    df1 = df.reindex([4, 2, 5, 3, 1])
    print(df1)
    df1 = df.reindex(columns=['지사', '연도'])
    print(df1)

def mysyntex_test_pandas_op_series():
    subject = subject_printer(mysyntex_test_pandas_op_series)

    # 동일.
    #s1 = pd.Series(range(0, 10, 2))
    #s1 = pd.Series(list(range(0, 10, 2))) 
    data = list(range(1, 6, 1))
    s1 = pd.Series(data)    
    s2 = pd.Series([x*2 for x in data if x <=3])
    print(s1)    
    print(s2)
    
    print(s1 + s2 + 5)
    print(s1 ** s2) # int64 -> float
    print(s1 > 3)

    #dict_data = {'a':1.0, 'b':2.0, 'c':3.0, 'd':4.0, 'e':5.0}
    #s1 = pd.Series(dict_data)
    #print(s1)
    index_data = ['a', 'b', 'c', 'd', 'e']
    data = [0.0, 1.0, 2.0, 3.0, 4.0]    
    s1 = pd.Series(data, index=index_data)
    print(s1)

    # selection  ----------------------------------
    #print(s1['a'])
    #print(s1[['a', 'c']])
    #print(s1['a':'c'])
    #print(s1[0])

    #print(s1[1])
    #print(s1[[1, 3]])
    #print(s1[1:3])    p
    #print(s1[(s1>1) & (s1%2==0)])

    #s1loc = s1.loc['a'] # dtype: float64    
    #s1loc = s1.loc[['a', 'c', 'e']] # series    
    #print(s1.loc['b':'d'])
    
    #print(s1.iloc[1])
    #print(s1.iloc[[0, 2, 4]])
    #print(s1.iloc[1:4])

    # assign ----------------------------------
    # s2 = s1[:]
    # s2.iloc[1:4] = 10
    # print(s1)
    # s2 = s1[:]
    # s2.loc['a':'c'] = 5
    # print(s1)

    # remove ----------------------------------
    s1 = s1.drop(index='a')
    print(s1)
    s1 = s1.drop(index=['b','c'])
    print(s1)

    # merge ----------------------------------
    s1 = pd.Series([1,2,3])
    s2 = pd.Series([10,20])
    s3 = pd.Series([100,200])
    print(pd.concat([s1, s2, s3]))
    print(pd.concat([s1, s2, s3], ignore_index=True))
    
    # append is defrecated.
    # s3 = s1[:]
    # print(s3)
    # s3.append(s2, ignore_index=True)
    # print(s3)

def mysyntex_test_pandas_op_dataframe():
    subject = subject_printer(mysyntex_test_pandas_op_dataframe)   

    l1 = list(range(1, 6, 1))   
    dict_data1 = {
        'A' : [x for x in l1],
        'B' : [x*10 for x in l1],
        'C' : [x*100 for x in l1]} 
    l1 = list(range(1, 5, 1))
    dict_data2 = {
        'A' : [x for x in l1],
        'B' : [x*10 for x in l1],
        'D' : [x*100 for x in l1]} 
    df1 = pd.DataFrame(dict_data1)
    df2 = pd.DataFrame(dict_data2)
    print(df1)
    print(df2)

    print(df1 + df2)
    print(df1 * df2)
    print(df1 > 30)

    print(df1.mean())
    print(df1.std())
    print(df1.mean(axis=1))
    print(df1.std(axis=1))
    print(df1.describe())

    index_data = ['a', 'b', 'c', 'd', 'e']
    df1 = pd.DataFrame(dict_data1, index=index_data)
    #print(df1)
    print(df1.loc['a'])
    print(df1.loc[['a', 'c', 'e']])
    print(df1.loc['a':'c'])
    
    print(df1.iloc[2])
    print(df1.iloc[[1, 3, 4]])
    print(df1.iloc[2:5])
    # df1.loc['a':'c'] = 5    
    # print(df1)
    # df1.iloc[1:3] = 4
    # print(df1)
    print(df1[df1['A'] > 3])
    # print(df1[df1['A'] > 3])
    print(df1[df1['A'].isin([3, 4])])
    print(df1.head(2))
    print(df1.tail(2))

    print(df1['A'])
    print(df1[['A']])
    print(df1[['A','C']])
    df1['A'] = 10
    print(df1)
    print(df1.loc['a', 'A'])
    print(df1.iloc[0,0])
    print(df1.loc['a':'c', ['A','B']])
    print(df1.iloc[0:3,0:2])
    print(df1.loc[df1['A']>2, ['A','B']])
    print(df1['A']['a'])
    print(df1['A'][2])
    print(df1['A'][[0,2,3]])
    print(df1['A']['a':'c'])
    print(df1['A'][df1['B']>=3])
    print(df1.T)

    df1 = df1.T
    df1 = df1.drop(index='A')
    print(df1)
    df1 = df1.drop(columns=['a', 'c'])
    print(df1)

    df1 = pd.DataFrame({'물리':[95,92,98,100],'수학':[85,82,88,80]})
    df2 = pd.DataFrame({'물리':[85,62],'수학':[75,72]})
    df3 = pd.DataFrame({'화학':[55,32]})
    df4 = pd.DataFrame({'물리':[55,32]})
    df5 = pd.DataFrame({'물리':[85,62], '화학':[75,72]})

    print(pd.concat([df1, df2, df3], ignore_index=True))
    print(pd.concat([df1, df2, df4], ignore_index=True, join='inner'))
    print(pd.concat([df1, df2, df3], axis=1))
    print(pd.concat([df1, df2, df3], axis=1, join='inner'))    


    # join  : 가로방향(인덱스기준) 병합
    # merge : 가로방향(열기준) 병합

    df1 = pd.DataFrame({'A':['a0', 'a1', 'a2', 'a3'], 'B':['b0', 'b1', 'b2', 'b3']})
    df2 = pd.DataFrame({'C':['c0', 'c1', 'c2'], 'D':['d0', 'd1', 'd2']}, index=[2,3,4])
    df3 = pd.DataFrame({'A':['a31', 'a32', 'a33'], 'D':['d0', 'd1', 'd2']}, index=[2,3,4])
    print(df1.join(df2, how='left'))    
    print(df1.join(df2, how='right'))
    print(df1.join(df2, how='outer'))
    print(df1.join(df2, how='inner'))

    print(df1.join(df3, how='outer', lsuffix='_1', rsuffix='_2'))
   

    # merge sample : 기준을 제외하고 겹치는 열이 없는 경우.
    code_list = ['LS05', 'SM10', 'BP70', 'LS10', 'BP70', 'SM10', 'LS05']
    sales_list = [29, 26, 30, 22, 19, 38, 45]
    store_list = ['강남', '강남', '강남', '대학로', '대학로', '인천공항', '인천공항']
    df1 = pd.DataFrame({'code':code_list, 'sale':sales_list,'stroe':store_list})    
    df2 = pd.DataFrame({
        'code':['LS05', 'SM10', 'BB70', 'BB20'],
        'name':['브리오슈','베이글','치아바타','바게트']})

    print(df1.merge(df2, how='left', on='code'))
    print(df1.merge(df2, how='right', on='code'))

    # merge sample : 기준을 제외하고 겹치는 열이 존재하는 경우.
    df1 = pd.DataFrame({
        'key':['k0', 'k1', 'k2', 'k3'],
        'A':['a0', 'a1', 'a2', 'a3']})

    df2 = pd.DataFrame({
        'key':['k2', 'k3', 'k4', 'k5'],
        'B':['b2', 'b3', 'b4', 'b5']})    
    
    print(df1.merge(df2, how='left', on='key'))    
    print(df1.merge(df2, how='right', on='key'))    
    print(df1.merge(df2, how='outer', on='key'))    
    print(df1.merge(df2, how='inner', on='key'))
    

    df1 = pd.DataFrame({
        'key':['k0', 'k1', 'k2', 'k3'],
        'A':['a0', 'a1', 'a2', 'a3'],
        'C':['c0', 'c1', 'c2', 'c3']})

    df2 = pd.DataFrame({
        'key':['k0', 'k1', 'k2', 'k3'],
        'A':['a0', 'a1', 'a4', 'a5'],
        'D':['d0', 'd1', 'd4', 'd5']})

    print(df1.merge(df2, how='inner'))
    print(df1.merge(df2, how='inner', on=['key', 'A']))
    print(df1.merge(df2, how='inner', on='key'))
    print(df1.merge(df2, how='inner', on='A'))
    print(df1.merge(df2, how='inner', on='A', suffixes=('_left', '_right')))


def mysyntex_test_pandas_dataframe_cvs():
    subject = subject_printer(mysyntex_test_pandas_dataframe_cvs)

    import numpy as np
    import pandas as pd

    dict_data = {
        '제품ID' : ['P1001', 'P1002', 'P1003', 'P1004'],
        '판매가격' : [5000, 7000, 8000, 10000],
        '판매량' : [40, 93, 70, 48]}
    df = pd.DataFrame(dict_data)
    print(df)

    #save
    #df.to_csv("product_sales.csv", encoding='cp949')
    df.to_csv("product_sales.csv", encoding='utf-8', index=False)

    #read
    df = pd.read_csv("product_sales.csv", sep=',', encoding='utf-8')
    print(df)

    df = pd.read_csv("product_sales.csv", sep=',', encoding='utf-8', header=None)
    print(df)

    columns_data = ['제품New', '판매가격New', '판매량New']
    df = pd.read_csv("product_sales.csv", sep=',', encoding='utf-8', names=columns_data)
    print(df)

    df = pd.read_csv("product_sales.csv", sep=',', encoding='utf-8', header=0, names=columns_data)
    print(df)


def mysyntex_test_pandas_dataframe_excel():
    subject = subject_printer(mysyntex_test_pandas_dataframe_excel)

    import numpy as np
    import pandas as pd

    dict_data = {
        '제품ID' : ['P1001', 'P1002', 'P1003', 'P1004'],
        '판매가격' : [5000, 7000, 8000, 10000],
        '판매량' : [40, 93, 70, 48]}
    df = pd.DataFrame(dict_data)
    print(df)

    #save
    df.to_excel("product_sales.xlsx")

    # excel_writer = pd.ExcelWriter("product_sales2.xlsx", engine='openpyxl')
    # df.to_excel(excel_writer, index=True, header=True, sheet_name='Sheet1', startrow=0, startcol=0)
    # df.to_excel(excel_writer, index=True, header=True, sheet_name='Sheet2', startrow=1, startcol=1)
    # excel_writer.save() # not public api    

    with pd.ExcelWriter("product_sales.xlsx", engine='xlsxwriter') as excel_writer:
    #with pd.ExcelWriter("product_sales.xlsx", engine='openpyxl') as excel_writer:
        df.to_excel(excel_writer, index=True, header=True, sheet_name='Sheet1', startrow=0, startcol=0)
        df.to_excel(excel_writer, index=True, header=True, sheet_name='Sheet2', startrow=1, startcol=1)
        df.to_excel(excel_writer, index=False, header=False, sheet_name='Sheet2', startrow=2, startcol=6)

    #read
    df = pd.read_excel("product_sales.xlsx")
    print(f'{"":{"-"}<{50}}')
    print(df)    

    df = pd.read_excel("product_sales.xlsx", index_col=0, header=0)
    print(f'{"":{"-"}<{50}}')
    print(df)

    name_list = ['제품New', '판매가격New', '판매량New']
    df = pd.read_excel("product_sales.xlsx", index_col=0, header=0, names=name_list)
    print(f'{"":{"-"}<{50}}')
    print(df)

    df = pd.read_excel("product_sales.xlsx", sheet_name='Sheet2')
    print(f'{"":{"-"}<{50}}')
    print(df)


import xlsxwriter
def mysyntex_test_xlsxwriter():
    subject = subject_printer(mysyntex_test_xlsxwriter)
    
    workbook = xlsxwriter.Workbook("test_xlsxwriter.xlsx")
    worksheet = workbook.add_worksheet("sheet1")
    worksheet.write(0, 0, 10)
    #worksheet.write('A0', 11)
    worksheet.write(1, 0, 100)
    worksheet.write(2, 0, 3.14)
    worksheet.write(3, 0, 'hi')
    worksheet.write(4, 0, '=COS(PI()/4)')
    worksheet.write(5, 0, None)

    worksheet.write(1, 1, 100)
    worksheet.write(2, 1, 200)
    worksheet.write(3, 1, 300)
    worksheet.write(4, 1, 400)
    worksheet.write(5, 1, '=SUM(B2:B5)')


    worksheet = workbook.add_worksheet("sheet2_new")
    list_num = list(range(1, 10, 1))
    for col, val in enumerate(list_num):
        worksheet.write(0, col, val)
        
    worksheet.write_row(1, 0, list_num)
    worksheet.write_column(2, 0, list_num)

    dict_data = {
        '제품ID':['P001', 'P002', 'P003'],
        '가격':[9999, 19999, 29999],
        '판매량':[50, 30, 40]}
    list_keys = list(dict_data.keys())
    list_values = list(dict_data.values())
    worksheet.write_row(20, 0, list_keys)
    for col, list_value in enumerate(list_values):
        worksheet.write_column(21, col, list_value)

    workbook.close()

def mysyntex_test_xlsxwriter_cellformat():
    subject = subject_printer(mysyntex_test_xlsxwriter_cellformat)
    
    workbook = xlsxwriter.Workbook("test_xlsxwriter_cellformat.xlsx")
    worksheet = workbook.add_worksheet("sheet1")

    #-----------------------------------------------------
    # 셀 서식 지정.
    cell_format = workbook.add_format({
        'font_name':'바탕',
        'bold':True,
        'font_color':'blue'})
    # 함수로 셀 서식 지정
    cell_format.set_italic()
    cell_format.set_font_size(20)

    worksheet.write('A1', '셀 서식 미지정')
    worksheet.write('A2', '셀 서식 지정', cell_format)

    
    #-----------------------------------------------------
    # 배경
    cell_fmt1 = workbook.add_format()
    cell_fmt2 = workbook.add_format()
    cell_fmt3 = workbook.add_format()

    cell_fmt1.set_bg_color('lime')
    cell_fmt2.set_bg_color('blue')
    cell_fmt2.set_font_color('white')
    cell_fmt3.set_bg_color('red')
    cell_fmt3.set_pattern(6) #배경 무늬 (0~18)
    cell_fmt3.set_font_color('#FFFFFF') #RGB

    worksheet.write('C1', "안녕")
    worksheet.write('C2', "안녕", cell_fmt1)
    worksheet.write('C3', "안녕", cell_fmt2)
    worksheet.write('C4', "안녕", cell_fmt3)


    #-----------------------------------------------------
    # 테두리
    cell_fmt1 = workbook.add_format()
    cell_fmt2 = workbook.add_format()
    cell_fmt3 = workbook.add_format()

    cell_fmt1.set_border(1)
    cell_fmt2.set_border(2)
    cell_fmt2.set_border_color('blue')
    cell_fmt3.set_bottom(8)
    cell_fmt3.set_left(6)    

    worksheet.write('D1', "안녕")
    worksheet.write('D2', "안녕", cell_fmt1)
    worksheet.write('D3', "안녕", cell_fmt2)
    worksheet.write('D4', "안녕", cell_fmt3)

    #-----------------------------------------------------
    # 숫자 형식
    cell_fmts = [workbook.add_format() for k in range(5)]
    for k in range(5):
        cell_fmts[k].set_num_format(k+1)
    
    num_data1 = 1234.567
    num_data2 = -1234.567

    worksheet.write('E1', num_data1)
    worksheet.write('F1', num_data2)

    for k in range(5):
        row = k+2
        idx = k+1
        worksheet.write(row, 3, idx)
        worksheet.write(row, 4, num_data1, cell_fmts[k])
        worksheet.write(row, 5, num_data2, cell_fmts[k])


    #-----------------------------------------------------
    # date 형식
    worksheet = workbook.add_worksheet("sheet2")
    
    datetime_formats = [
        'm/d/yy',
        'd-mmm-yyy',
        'd-mmm',
        'mmm-yy',
        'h:mm AM/PM',
        'h:mm:ss AM/PM',
        'h:mm',
        'h:mm:ss',
        'm/d/yy h:mm',
        'yyyy"년" mm"월" dd"일"',
        'yyyy"년" mm"월" dd"일" hh:mm:ss',
        'yy"년" m"월" d"일"',
        'yy"년" m"월" d"일" hh:mm:ss']
    
    cell_formats = [workbook.add_format() for k in range(13)]

    for k in range(13):
        if(k < 9):
            cell_formats[k].set_num_format(k+14)
        else:
            cell_formats[k].set_num_format(datetime_formats[k])
    
    datetime_data = datetime(2021, 4, 8, 17, 38, 59)

    cell_format = workbook.add_format({'bold':True})
    worksheet.write(0,0, '인덱스', cell_format)
    worksheet.write(0,1, '서식 지정 문자열', cell_format)
    worksheet.write(0,2, '서식 지정 출력 결과', cell_format)

    # write cell
    for k in range(13):
        index = k+14
        row = k+1
        if(k<9):
            worksheet.write(row, 0, index)
        else:
            worksheet.write(row, 0, "한글 날짜 서식 지정")
        
        worksheet.write(row, 1, datetime_formats[k])
        worksheet.write(row, 2, datetime_data, cell_formats[k])


    #-----------------------------------------------------
    # align / w/h
    worksheet = workbook.add_worksheet("sheet3")
    cell_fmt1 = workbook.add_format({'align':'left'})
    cell_fmt2 = workbook.add_format({'align':'center'})
    cell_fmt3 = workbook.add_format({'align':'right'})
    cell_fmt4 = workbook.add_format({'valign':'top'})
    cell_fmt5 = workbook.add_format({'valign':'vcenter'})
    cell_fmt6 = workbook.add_format({'valign':'bottom'})

    worksheet.set_row(0, 20)
    worksheet.set_row(1, 40)
    worksheet.set_row(2, 60)
    worksheet.set_column(0, 0, 15)
    worksheet.set_column(1, 2, 30)

    for k in range(3):
        worksheet.write(0, k, "정렬, 크기", cell_fmt1)
        worksheet.write(1, k, "정렬, 크기", cell_fmt2)
        worksheet.write(2, k, "정렬, 크기", cell_fmt3)
        worksheet.write(3, k, "정렬, 크기", cell_fmt4)
        worksheet.write(4, k, "정렬, 크기", cell_fmt5)
        worksheet.write(5, k, "정렬, 크기", cell_fmt6)


    #-----------------------------------------------------
    # insert image
    worksheet = workbook.add_worksheet("insert-image")
    image_file = "동구리.gif"
    worksheet.insert_image(8, 1, image_file, {
        'x_offset':25, 'y_offset':10,'x_scale':5, 'y_scale':5})

    optinos = {
        'x_offset':25, 'width':240, 'height':150,
        'align':{'vertical':'middle', 'horizontal':'center'},
        'font':{'bold':True, 'size':15},
        'boder':{'color':'black', 'width':2},
        'fill':{'color':'yellow'}
    }
    worksheet.insert_textbox(8, 20, '텍스트박스', optinos)

    workbook.close()

import xlwings as xw
import numpy as np
def mysyntex_test_xlwings():
    subject = subject_printer(mysyntex_test_xlwings)

    wb = xw.Book()
    sht = wb.sheets['Sheet1'] # 이미 존재하는 Sheet 를 가져옴.

    sht.range((1,1)).value = 100
    sht.range((2,1)).value = 3.14
    sht.range((3,1)).value = 'hi'

    sht.range('B1').value = 100
    sht.range('B2').value = 3.14
    sht.range('B3').value = 'hi'
    sht.range('B4').value = '=sum(B1:B2)'

    print(sht.range('A1').value)
    print(sht.range('A2').value)
    print(sht.range('A3').value)


    sht = wb.sheets['Sheet2']
    list_data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    sht.range((1,1)).value = '리스트'
    sht.range((2,1)).value = list_data
    
    npdata = np.array([10, 20, 30, 40, 50])
    sht.range('A6').value = '넘파이 배열'
    sht.range((7,1)).value = npdata

    pddata = pd.Series([10, 20, 30, 40, 50])
    sht.range('A9').value = '판다스 Series'
    sht.range((10,1)).value = pddata

    pddata = pd.DataFrame(list_data, columns=['A', 'B', 'C'])
    sht.range('A16').value = '판다스 dataframe'
    sht.range((17,1)).value = pddata


    wb.save("xlwings_test.xlsx")
    wb.close()


    wb = xw.Book("xlwings_test.xlsx")
    sht = wb.sheets['Sheet2'] # 이미 존재하는 Sheet 를 가져옴.
    list_data = sht.range('A2').options(expand='table').value
    print(list_data)

    array_data = sht.range('A7').options(np.array, expand='table').value
    print(array_data)

    series_data = sht.range('A10').options(pd.Series, expand='table', header=False).value
    print(series_data)
    series_data = sht.range('B10').options(pd.Series, expand='table', header=False, index=False).value
    print(series_data)

    df_data = sht.range('A17').options(pd.DataFrame, expand='table').value
    print(df_data)
    df_data = sht.range('B17').options(pd.DataFrame, expand='table', index=False).value
    print(df_data)


    #상대경로가 여기가 아님
    #sht.api.PrintOut()
    #sht.api.ExportAsFixedFormat(0, "xlwings_test.pdf")
    wb.api.ExportAsFixedFormat(0, "xlwings_test.pdf")


def mysyntex_test_read_html():
    subject = subject_printer(mysyntex_test_read_html)

    url = 'https://search.naver.com/search.naver?stop_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
    #url = 'https://finance.naver.com/item/coinfo.naver?code=005930'
    dfs = pd.read_html(url)
    print(len(dfs))
    print(dfs)
    
    exchange_rate_df = dfs[0].replace({'전일대비상승':'▲', '전일대비하락':'▼'}, regex=True)
    print(exchange_rate_df)

    excel_filepath = "html_to_excel.xlsx"
    exchange_rate_df.to_excel(excel_filepath, index=False)

    url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
    dfs = pd.read_html(url, header=1)    
    #print(dfs)
    dfs9 = dfs[0].head(9)
    print(dfs9)
    dfs9.to_excel("html_to_excel9.xlsx", index=False)


def mysyntex_test_excel_chart():
    subject = subject_printer(mysyntex_test_excel_chart)

    excel_file = 'chart.xlsx'
    excel_chart_file = 'chart_out.xlsx'
    df = pd.read_excel(excel_file)
    print(df)    

    worksheet_name = 'Sheet1'

    excel_writer = pd.ExcelWriter(excel_chart_file, engine='xlsxwriter')
    df.to_excel(excel_writer, sheet_name=worksheet_name, index=False)    

    workbook = excel_writer.book
    worksheet = excel_writer.sheets[worksheet_name]

    # 세로 막대형 차트
    #chart = workbook.add_chart({'type':'column'})
    #chart = workbook.add_chart({'type':'line'})
    chart = workbook.add_chart({'type':'area', 'subtype':'stacked'})

    """
    # 차트 데이터 범위 지정
    chart.add_series({'values': '=Sheet1!B2:B7'})
    chart.add_series({'values': '=Sheet1!C2:C7'})
    chart.add_series({'values': '=Sheet1!D2:D7'})
    """

    column_len = len(df.columns)
    for k in range(column_len -1):
        start_row = 1               # 범위 시작 행 번호
        start_col = k + 1           # 범위 시작 열 번호
        end_row = len(df.index)     # 범위 끝 행 번호
        end_col = k+1               # 범위 끝 열 번호

        chart.add_series({
            'values': [worksheet_name, start_row, start_col, end_row, end_col], # 데이터
            'categories' : [worksheet_name, start_row, 0, end_row, 0], # 축(행) 범례
            'name': [worksheet_name, 0, k+1], # 열 범례
            'overlap': [-15]}) # 그래프 사이 간격

    chart.set_title({'name': '영업팀 별 하반기 판매현황'})
    chart.set_x_axis({'name': '월'}) #행
    chart.set_y_axis({'name': '판매현황'}) #열

    # 차트 위치 지정, 삽입
    worksheet.insert_chart('E2', chart, {'x_offset':25, 'y_offset':10})

    excel_writer.save()

def mysyntex_test_excel_sheet2_chart():
    subject = subject_printer(mysyntex_test_excel_sheet3_chart)

    excel_file = 'chart.xlsx'
    excel_chart_file = 'chart_out2.xlsx'
    worksheet_name = 'Sheet2'

    df = pd.read_excel(excel_file, sheet_name=worksheet_name)
    print(df)     

    excel_writer = pd.ExcelWriter(excel_chart_file, engine='xlsxwriter')
    df.to_excel(excel_writer, sheet_name=worksheet_name, index=False)    

    workbook = excel_writer.book
    worksheet = excel_writer.sheets[worksheet_name]
    
    chart = workbook.add_chart({'type':'pie'})

    column_len = len(df.columns)

    for k in range(column_len - 1):        
        start_row = 1               # 범위 시작 행 번호
        start_col = k+1           # 범위 시작 열 번호
        end_row = len(df.index)     # 범위 끝 행 번호
        end_col = k+1               # 범위 끝 열 번호

        chart.add_series({
            'values': [worksheet_name, start_row, start_col, end_row, end_col], # 데이터
            'categories' : [worksheet_name, start_row, 0, end_row, 0], # 축(행) 범례
            'name': [worksheet_name, 0, k+1],
            'data_labels':{
                'value':True,
                'percentage':True,
                'category':True,
                'position':'outside_end'}})

    chart.set_title({'name': '가장 좋아하는 운동 조사 결과'})        
    chart.set_legend({'position':'bottom'}) #범례 표시하지 않음.
    chart.set_style(1)

    # 차트 위치 지정, 삽입
    worksheet.insert_chart('E2', chart, {'x_offset':25, 'y_offset':10})

    excel_writer.save()

def mysyntex_test_excel_sheet3_chart():
    subject = subject_printer(mysyntex_test_excel_sheet3_chart)

    excel_file = 'chart.xlsx'
    excel_chart_file = 'chart_out3.xlsx'
    worksheet_name = 'Sheet3'

    df = pd.read_excel(excel_file, sheet_name=worksheet_name)
    print(df)     

    excel_writer = pd.ExcelWriter(excel_chart_file, engine='xlsxwriter')
    df.to_excel(excel_writer, sheet_name=worksheet_name, index=False)    

    workbook = excel_writer.book
    worksheet = excel_writer.sheets[worksheet_name]
    
    chart = workbook.add_chart({'type':'scatter'})

    column_len = len(df.columns)
    start_row = 1               # 범위 시작 행 번호
    start_col = 1           # 범위 시작 열 번호
    end_row = len(df.index)     # 범위 끝 행 번호
    end_col = 1               # 범위 끝 열 번호

    chart.add_series({
        'values': [worksheet_name, start_row, start_col, end_row, end_col], # 데이터
        'categories' : [worksheet_name, start_row, 0, end_row, 0], # 축(행) 범례
        'maker': {'type':'circle', 'size':10}})

    chart.set_title({'name': '키와 몸무게의 관계'})
    chart.set_x_axis({
        'name': '키 (cm)',
        'min':150, 'max':190,
        'major_gridlines':{'visible':True}}) #행
    chart.set_y_axis({
        'name': '몸무게 (kg)',
        'min':40, 'max':100}) #열

    chart.set_legend({'position':'none'}) #범례 표시하지 않음.

    # 차트 위치 지정, 삽입
    worksheet.insert_chart('E2', chart, {'x_offset':25, 'y_offset':10})

    excel_writer.save()

def mysyntex_test_excel_sheet4_chart():
    subject = subject_printer(mysyntex_test_excel_sheet4_chart)

    excel_file = 'chart.xlsx'
    excel_chart_file = 'chart_out4.xlsx'
    worksheet_name = 'Sheet4'

    df = pd.read_excel(excel_file, sheet_name=worksheet_name)
    print(df)     

    excel_writer = pd.ExcelWriter(excel_chart_file, engine='xlsxwriter')
    df.to_excel(excel_writer, sheet_name=worksheet_name, index=False)    

    workbook = excel_writer.book
    worksheet = excel_writer.sheets[worksheet_name]
    
    chart = workbook.add_chart({'type':'scatter'})

    column_len = len(df.columns)

    for k in range(len(df.index)):
        start_row = k+1               # 범위 시작 행 번호
        end_row = start_row
        market_share = df.iloc[k,3]
        circle_size = int(15 + market_share * 1.1)
        if circle_size > 72:
            circle_size = 72

        chart.add_series({
            'values': [worksheet_name, start_row, 2, end_row, 2], # 데이터
            'categories' : [worksheet_name, start_row, 1, end_row, 1], # 축(행) 범례
            'name':[worksheet_name, start_row, 0],
            'maker': {
                'type':'circle',
                'size': circle_size},
            'data_labels':{'value':True, 'position':'center'}})

        chart.set_title({'name': '시장 점유율 비교'})
        chart.set_x_axis({
            'name': '판매량',
            'min':0, 'max':10,
            'major_gridlines':{'visible':True}}) #행
        chart.set_y_axis({
            'name': '판매가격 (억)',
            'min':0, 'max':8}) #열

    #chart.set_legend({'position':'none'}) #범례 표시하지 않음.

    # 차트 위치 지정, 삽입
    worksheet.insert_chart('E2', chart, {'x_offset':25, 'y_offset':10})

    excel_writer.save()


# # math test
# import math
# math.sqrt()
# math.pi
# round()

# import random
# num = random.random()
# num = random.ranint(0, 1000)
# num = random.ranrange(0, 1000, 5)
# color = random.choice(["red", "black", "green"])

#mysyntex_test_sys()
#mysyntex_test_print()
#mysyntex_test_type()
#mysyntex_test_branch()
#mysyntex_test_loop()
#mysyntex_test_class()
#mysyntex_test_list()
#mysyntex_test_tuple()
#mysyntex_test_dict()
#mysyntex_test_string()
#mysyntex_test_array()
#mysyntex_test_fileio()
#mysyntex_test_fileio_encoding()
#mysyntex_test_fileio_json()

#mysyntex_test_module()
#mysyntex_test_module_pathlib()    
#mysyntex_test_module_datetime()
#mysyntex_test_module_locale()

#mysyntex_test_numpy()
#mysyntex_test_pandas()
#mysyntex_test_pandas_dataframe()
#mysyntex_test_pandas_op_series()
#mysyntex_test_pandas_op_dataframe()
#mysyntex_test_pandas_dataframe_cvs()
#mysyntex_test_pandas_dataframe_excel()

#mysyntex_test_xlsxwriter()
#mysyntex_test_xlsxwriter_cellformat()
#mysyntex_test_xlwings()
#mysyntex_test_read_html()

#mysyntex_test_excel_chart()
mysyntex_test_excel_sheet2_chart()
mysyntex_test_excel_sheet3_chart()
mysyntex_test_excel_sheet4_chart()

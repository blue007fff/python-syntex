# 파이썬 기본 문법 정리

class subject_printer:
    def __init__(self, function):
        print(f'{"":{"="}<{50}}')
        print(f'{function.__name__ :{"="}<{50}}')   
        print(f'{"":{"="}<{50}}')

    def __del__(self):        
        print(f'{"":{"_"}<{50}}')
        print("")



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

#mysyntex_test_module()
#mysyntex_test_module_pathlib()    
#mysyntex_test_module_datetime()
mysyntex_test_module_locale()

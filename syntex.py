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


#mysyntex_test_print()
#mysyntex_test_type()
#mysyntex_test_branch()
#mysyntex_test_loop()
#mysyntex_test_class()
#mysyntex_test_list()
mysyntex_test_string()

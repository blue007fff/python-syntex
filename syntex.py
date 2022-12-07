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
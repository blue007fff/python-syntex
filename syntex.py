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

    print('{:<15}'.format('padding'))
    print('{:>15}'.format('padding'))
    print('%15s' % ('padding'))
    print('%-15s' % ('padding'))


mysyntex_test_print()
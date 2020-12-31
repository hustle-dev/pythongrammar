# 파이썬의 함수 구조
'''
def 함수명(매개변수) :
    <수행할 문장1>
    <수행할 문장2>
    ...
'''

def add(a, b):
    return a+b

a = 3
b = 4
c = add(a,b)
print(c)

# 입력값이 모르는 함수
'''
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
'''

def add_many(*args):
    result = 0
    for i in args:
        result = result+i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

'''
키워드 파라미터 kwargs
def print_kwargs(**kwargs):
     print(kwargs)
'''

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3)

# 파이썬에서 함수의 리턴값이 여러개일때 하나의 변수로 받으면 그 변수에 튜플로 해서 값이 들어감.

# 매개변수 초깃값 미리 설정하는 것 가능
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나의 이름은 %d 살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
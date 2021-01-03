'''
라이브러리 함수 정리
abs(x) --> x의 절댓값을 돌려주는 함수
all(x) --> 반복가능한 자료형 x를 입력인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려줌
all([1, 2, 3, 0]) --> false (0 때문에)
any(x) --> all과 달리 요소가 하나라도 참이면 True를 반환하고 x가 모두 거짓인 경우에만 false를 돌려줌 (all 의 반대)
chr(x) --> 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력
dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
input([prompt])은 사용자 입력을 받는 함수이다.
int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
'''

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times_map(x):
    return x*2

print(list(map(two_times_map, [1,2,3,4])))
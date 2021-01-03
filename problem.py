#Q1
str1 = "a:b:c:d"
print(str1.replace(":", "#"))

#Q2
a = {'A' : 90, 'B' : 80}
if 'C' not in a:
    a['C'] = 70

print(a['C'])
'''
a.get('C', 70) get 함수를 이용해서 다음과 같이 딕셔너리에 'C'가 없을때 70을 반환하게 할 수 있음!
'''

#Q3
a = [1, 2, 3]

a = a + [4, 5] # 기존 a의 주소와 다른 a를 돌려줌
print(a)

a = [1,2,3]
a.extend([4,5]) # 기존 a의 주소값과 같음
print(a)

#Q4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum1 = 0
for a in A:
    if a >50:
        sum1 += a
print(sum1)


#Q5
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)


n = input()
for i in range(int(n)):
    print(fib(i))

#Q1
a = 80
b = 75
c = 55
avg = (a+b+c)/3
print(avg)

#Q2
a = 13 % 2

#Q3
a = '881120-1068234'
print(a[:6])
print(a[7:])

#Q4
print(a[7])

#Q5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

#Q6
a = [1,3,5,4,2]
a.sort()
a.reverse
print(a)

#Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#Q8
a = (1,2,3)
a += (4,)
print(a)

#Q9
# a[[1]]인 경우 오류 발생 key는 고유해야하는데 list가 변하므로 오류 발생

#Q10
a = {'A': 90, 'B':80, 'C':70}
print(a.pop('B'))

#Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
a = set(a)
print(a)
b = list(a)
print(b)

#Q12
#동일한 값에 여러개의 변수를 선언하게 되면 ex) a = b =[1,2,3] 인 경우 a와 b는 둘다 같은공간을
#가리키고 있기 때문에 a[1] = 4로 요소를 바꾸게 되면 b도 똑같이 적용이됨!
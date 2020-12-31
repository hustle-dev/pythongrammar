#Q1
def is_odd(num):
    if(num % 2 == 0):
        print("This is not odd")
    else:
        print("This is odd")

is_odd(10)

#Q2
def avg(*args):
    sum = 0
    for i in args:
        sum += i
    return (sum / len(args))

a = avg(1,2,3,4,5)
print(a)

#Q3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % total)

#Q4
#3번.

#Q5
f1 = open("test.txt", "w")
f1.write("Life is too short") # 파일을 쓰고나서 무조건 닫아야만 저장된 데이터를 읽을 수 있음!
f1.close()
'''
with open("test.txt", "w") as f1:
    f1.write("Life is too short!")
'''

f2 = open("test.txt", "r")
print(f2.read())
f2.close()

#Q6
userinput = input("아무거나 입력하시오:")
with open("user.txt", "a") as u1:
    u1.write(userinput)

with open("user.txt", "r") as u2:
    print(u2.read())

#Q7
with open("test1.txt", "r") as q:
    data = q.read()

data = data.replace("java", "python")

with open("test1.txt", "w") as q2:
    q2.write(data)

with open("test1.txt", "r") as q3:
    print(q3.read())


    
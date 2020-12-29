test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


add = 0
for i in range(1, 11):
    add = add + i

print(add)


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')


# 리스트 내포 --> 리스트 안에 for 문을 포함하는 것
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 리스트 내포의 일반문법 [표현식 for 항목 in 반복가능객체 if 조건문]
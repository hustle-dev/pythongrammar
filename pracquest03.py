#Q1 --> shirt!
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print('')
#Q2
su = 0
i = 1
while i < 1001:
    if i % 3 == 0:
        su += i
    i += 1
    continue
print(su)

print('')
#Q3
i = 0
j = 1
while 1:
    while i<j:
        if i<j:
            print('*', end='')
            i += 1
    i = 0
    j += 1
    print('')
    if j == 6:
        break

#Q4
for n in range(1, 101):
    print(n)

print('')
#Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sumg = 0
for grade in A:
    sumg += grade
print(sumg / len(A))

print('')

#Q6
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
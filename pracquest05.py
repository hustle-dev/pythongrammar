#Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#Q3
# all([1,2,abs(-3)-3]) // false
# chr(ord('a') == 'a') // true

#Q4
print(list(filter(lambda x: x>0,[1, -2, 3, -5, 8, -3])))

#Q5
print(int('0xea', 16))

#Q6
print(list(map(lambda x: x*3, [1,2,3,4])))

#Q7
list1 = [-8, 2, 7, 5, -3, 5, 0, 1]
a = max(list1)
b = min(list1)
result = a+b
print(result)

#Q8
print(round(17/3, 4))

#Q9
'''
import sys

numbers = sys.argv[1:]

result = 0
for numeber in numbers:
    result += int(number)
print(result)
'''

#Q10

#Q11

#Q12

#Q13
import random
a = []

while len(a) <6:
    b = random.randint(1,45)
    if b not in a:
        a.append(b)
print(a)
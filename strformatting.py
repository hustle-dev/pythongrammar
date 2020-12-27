print("I eat %d apples." %3)
print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

num1 = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (num1, day))

print("Error is %d%%." % 98)
# %를 출력하고 싶을 때는 단순히 %하나만 쓰는 것이 아닌 두개를 같이 써주어야함! %%

# ----------------------------------------

# format 함수를 사용한 포매팅

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number2 = 3
print("I eat {0} apples" .format(number2))

# 2개 이상의 값 포매팅
num2 = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(num2, day))

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days" .format(number=10, day=3))

print("{{ and }}".format())


# f문자열 포매팅
nameh = '홍길동'
ageh = 30
print(f'나의 이름은 {nameh}입니다. 나이는 {ageh}입니다.')
a = "Life is too short, You need Python"
print(a[0:4])
# a[0:4]의 경우 0문자열 부터 3까지 출력

b = "20010331Rainy"
date = b[:8]
weather = b[8:]
print(date)
print(weather)

c = "Pithon"
print(c[:1] + 'y' + c[2:])
# Pithon의 배열 요소인 a[1]을 바로 바꾸는 것은 불가! -> 문자열의 요소값은 immutable한 자료형


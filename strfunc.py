a = "hobby"
print(a.count('b'))

b = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # 존재하지 않는경우 -1 반환!

# index의 경우 find와 마찬가지로 문자열 중 문자가 처음나온 위치를 반환하고 존재하지 않는경우 
# 오류 발생시킴!! <-- find와 다른 점!

# 문자열 삽입
print(",".join('abcd'))

# 소문자 -> 대문자 upper, 대 -> 소 lower 

# 왼쪽 공백 지우기: lstrip, 오른쪽 공백 지우기: rstrip(), 양쪽 공백: strip

# 문자열 바꾸기: replace(바뀌게 될 문자열, 바꿀 문자열)

# 문자열 나누기: split() --> 리스트로 나누어줌 
c = "Life is too short"
print(c.split())
d = "a:b:c:d"
print(d.split(':'))
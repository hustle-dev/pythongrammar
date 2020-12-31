f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data) # write함수를 통해 파일에다가 글을 씀
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline() # readline함수를 통해 한줄 씩 읽어오는 것
    if not line: break
    print(line)
f.close()

# readlines 함수는 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려줌 <-> readline과 차이 조심!
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read함수는 파일의 내용 전체를 문자열로 돌려줌

# 파일에 내용을 추가할때 'a'로 열기

# with문 --> f.close()를 따로 안해주어도 열고 닫기를 한번에 하게 해줌

'''
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
'''
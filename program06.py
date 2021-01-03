def GuGu(n):
    result = []
    i = 1
    while i<10:
        result.append(n*i)
        i = i+1
    return result
    
print(GuGu(2))

#06-2
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: 
        result += n
print(result)

#06-3
def getTotalPage(m ,n):
    if m % n == 0:
        return m // n
    else:
        return (m // n) + 1

print(getTotalPage(31, 10))

#06-4
'''
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open("memo.txt", 'a')
    f.write(memo)
    f.write('\n')
    f.close()
else option == '-v':
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)
'''

#06-5
'''
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', " "*4)

f = open(dst, "w")
f.write(space_content)
f.close()
'''

#06-6
'''
import os
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)
search("c:/")

디렉터리와 파일을 검색하는 일반적인 경우엔 os.walk사용을 추천!
'''
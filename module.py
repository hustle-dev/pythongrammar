def add(a,b):
    return a + b
def sub(a, b):
    return a-b


# 위와 같은 모듈이 있다고 하였을 시 모듈을 불러오는 방법은 이 파일의 이름인 module을 import 하는 것! --> import module
# import module 선언 시 위으 메서드를 사용하는 방법은 module.add(a,b) 다음과 같이 사용 하지만 바로 모듈 이름을 붙이지 않고 바로 사용하는 방법은 다음과 같음
# from module import add --> add(a,b) 와 같이 사용할 수 있음 또는 from module import * 을 사용하여 전체를 사용하겠다는 것을 알려줌


# if __name__ == "__main__":
#   print(add(1,4))
#   print(sub(4,2))

# 위의 if__name__ == "__main__" 은 python에서 직접 실행하였을 시 밑의 코드를 실행하라는 의미이며 그냥 import해서 써오는 경우 저 코드들을 실행하지 않음!

# python의 환경변수나 sys 모듈(sys.path.append)을 사용하여 다른 파일에 있는 모듈을 불러올 수 있다.
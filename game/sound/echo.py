def echo_test():
    print("echo")

# __init__.py 의 용동는 해당 디렉터리가 패키지의 일부임을 알려주는 역할!
# *을 사용한 import를 할 때 이곳에 정의돈 echo 모듈만 import를 한다는 __all__을  __init__.py에다가 적용을 해주어여함!
# ex __all__ = ['echo']
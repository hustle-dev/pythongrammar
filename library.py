'''
library 정리
sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
ex) C:/User/home>python test.py abc pey guido
명령 행에서 인수 전달 하기 --> sys.argv
강제로 스크립트 종료하기 --> sys.exit()
자신이 만든 모듈 불러와 사용하기 --> sys.path (''은 현재 디렉터리를 의미함)

pickle --> 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈.
pickle.dump(data, f)와 같이 사용하여 파일에 객체 data를 저장할 수 있음
pickle.load(f)를 사용하여 dump로 저장한 파일을 그대로 불러 올 수 있음

os --> 환경 변수나 디렉터리, 파일등의 os자원을 제어할 수 있게 해주는 모듈!
os.environ['PATH']
디렉터리 위치 변경하기 - os.chdir
디렉터리 위치 돌려받기 - os.getcwd
시스템 명령어 호출하기 - os.system
실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
os.mkdir(디렉터리)	디렉터리를 생성한다.
os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
os.unlink(파일)	파일을 지운다.
os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.

shutil은 파일을 복사해 주는 파이썬 모듈이다.
>>> import shutil
>>> shutil.copy("src.txt", "dst.txt")

디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

time.sleep 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다. 

calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다. 

random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.
일반 random()의 경우 0.0~1.0사이의 실 중에서 난수 값을 돌려줌
random.randint(1, 10) --> 1~10사이의 정수

webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 다음 예제는 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.

>>> import webbrowser
>>> webbrowser.open("http://google.com")
'''

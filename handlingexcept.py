# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("Very fast")

eagle = Eagle()
eagle.fly()

class Myerror(Exception): # __str__메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise Myerror()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except Myerror as e:
    print(e)


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


# try... finally의 경우 finaly는 예외 발생 여부에 상관없이 항상 수행되기 때문에 보통 리소스를 close하는 경우에 만힝 사용함(file close)
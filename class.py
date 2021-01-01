class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourcal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


# 클래스의 상속
class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourcal(4, 2)
print(b.pow())

# 메서드 오버라이딩
class SafeFourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourcal(4, 0)
print(c.div())

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

d = Family()
e = Family()
print(d.lastname)
print(e.lastname)

Family.lastname = "박"
print(d.lastname)
print(e.lastname)

# 객체변수는 클래스 변수를 공유하고 있음(id 값이 같음)
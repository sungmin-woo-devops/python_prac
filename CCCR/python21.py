# 사칙연산 클래스에 곱셈(mul), 뺄셈(sub), 나눗셈(div) 기능 추가
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        self.result = self.first + self.second
        return self.result
    
    def mul(self):
        self.result = self.first * self.second
        return self.result
    
    def sub(self):
        self.result = self.first - self.second
        return self.result

    def div(self):
        self.result = self.first / self.second
        return self.result

a = FourCal()
a.setdata(4, 2)

print(a.mul())
print(a.sub())

# __init__ : 생성자
# 생성자는 객체를 생성할 때 실행할 코드를 담고 있음
# ex) a = FourCal() - a를 만들면서 초깃값을 넣어주면 어떨까? 

# setdata() 함수를 __init__으로 변경
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        self.result = self.first + self.second
        return self.result
    
    def mul(self):
        self.result = self.first * self.second
        return self.result
    
    def sub(self):
        self.result = self.first - self.second
        return self.result

    def div(self):
        self.result = self.first / self.second
        return self.result

a = FourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 클래스의 상속
# 부모 클래스가 가지고 있는 메서드, 속성을 자식 클래스가 물려받게 됨
# 부모로부터 상속받은 메서드 등을 변경할 수 있다.

# 부모: FourCal / 자식: MoreFourCal
class MoreFourCal(FourCal): # 상속할 클래스를 괄호 안에 넣어줌
    pass

b = MoreFourCal(5, 2)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# 자식 클래스만의 코드 추가 가능
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreFourCal(5, 3)
print(c.pow())

# div 0 에러(ZeroDivisionError)
# 자식 클래스에서 div 메서드를 이용한 4 / 0 연산 수행
# d = MoreFourCal(4,0) 
# print(d.div()) # ZeroDivisionError

# 메서드 오버라이딩
# 부모로부터 상속받은 메서드를 자식 클래스에서 재정의
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

e = SafeFourCal(4, 0)
print(e.div())





# 클래스

# 장고에서의 클래스와 파이썬의 클래스는 다른 개념이다.
# 장고에서 class는 데이터베이스에 저장될 테이블을 의미함

# 변수, 함수는 선언하는 순간 메모리에 저장된다. -> 이렇게 메모리에 올라간 객체(object)라 한다.
# 클래스는 객체들의 집합이다.


# 함수를 사용한 계산기 코드
result = 0
def add(num):
    global result
    result = result + num
    return result

print(add(3))
print(add(4))

# 계산기2
result2 = 0
def add2(num):
    global result2
    result2 = result2 + num
    return result2

print(add2(3))
print(add2(4))

# 위의 경우처럼 동일한 함수의 코드를 반복해서 작성하는 경우 메모리 활용에 있어서 비효율적이다.
# = 코드 재사용성이 높아져 메모리를 효율적으로 사용할 수 있다.

# 클래스를 사용한 계산기 코드
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result = self.result + num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))

# 과자틀 = 클래스 / 과자 = 객체
# 과자 하나 먹는다고 다른 과자에 영향을 끼치지 않는다.
# = 객체 간 영향 X

# 클래스로 만들어진 객체는 서로에게 영향을 미치지 않음
print(id(cal1))
print(id(cal2))

# 객체를 사용한 후 제거 가능
del cal2

# 클래스 생성
class Cookie:
    pass

# 클래스 기반으로 객체 생성
a = Cookie()
b = Cookie()

print(a, type(a))

# a = Cookie()
# a는 객체, Cookie는 클래스
# a의 관점: a는 "Cookie 클래스의 인스턴스"


# 사칙연산
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        # self.a에 a 값을 넣어 self에 귀속시켜준다.
    
    def add(self): 
        # 이미 setdata()에서 인자 받았기에 추가적으로 호출할 필요 X
        # result는 add 메서드 내 지역변수(self. 지시자 없음)
        result = self.first + self.second
        return result

# self 매개변수가 있어야 클래스로 객체 생성 시
# 객체가 자기자신을 참조하여 메서드 혹은 어트리뷰트를 사용할 수 있다.

# 객체 사용 방법 1 (권장)
a = FourCal()
a.setdata(10, 20)

print(a.first)
print(a.second)
print(a.add())

# 객체 사용 방법 2
b = FourCal()
FourCal.setdata(b, 1, 3)
# 에러가 발생하는 목적
# 사용자가 잘못된 코드를 사용하는 상황을 막아 
# 프로그램이 잘못 동작하는 것을 방지하는데 사용된다.

# 에러를 처리하는 방법
# try ~ except
a, b = 4,0
try:
    c = a / b
    print(c)
except:
    print("error")

# 특정 에러 처리
# except: 담당 에러 처리
a, b = 4,0
try:
    c = a / b
    print(c)
    d = [1,2]
    print(d[5])
except SyntaxError:
    print("SyntaxError")
except ZeroDivisionError:
    print("ZeroDivisionError")

# 참고자료
# try-execept - https://blockdmask.tistory.com/537
# raise - https://blockdmask.tistory.com/538


# 에러 상세 표시
# except에서 지정한 에러의 상세 내용을 as 키워드로 받아 조회할 수 있다.
a, b = 4,0
try:
    c = a / b
    print(c)
    d = [1,2]
    print(d[5])
except SyntaxError:
    print("SyntaxError")
except ZeroDivisionError as e:
    print(e) # division by zero

##################################################################

# finally 
# try 블록에서 에러가 발생하고 난 뒤의 코드는 실행되지 않고
# except 블록으로 넘어가기 때문에 
# 에러 발생 뒤의 코드도 실행해주기 위해 finally 키워드를 사용한다.

try:
    4 / 0
except:
    print("error")
finally:
    print("무조건 실행")

# try 블록에서 except 구문 후에 finally에 포함된 쿠문 실행 후 종료된다.

# finally는 에러 발생 여부와 상관없이 무조건 실행된다.

##################################################################

# else
# try - except - else 구문
# else는 try에서 에러가 발생하지 않은 경우 실행되는 부분이다.

try:
    age = int(input("나이를 입력해주세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 19:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")

##################################################################

# 에러 넘기기
try:
    f = open("나없는파일", "r")
except:
    pass

##################################################################

# 에러 만들기 
# Exception 클래스, raise() 함수
class MyError(Exception):
    # 문자열 처리 후 class에 귀속된다.
    # print vs. __str__
    def __str__(self):
        return "허용되지 않는 에러입니다."
    
def MyError2():
    raise MyError()

print(MyError2())

# 참고자료
# __str__
# 1. https://recordnb.tistory.com/47

# __str vs. __repr__
 
##################################################################


# try + finally
# finally는 에러가 발생해도, 발생하지 않아도 무조건 거치는 구문
# except 없이 try + finally만 사용한다면
# 에러가 발생한 후 finally 구문까지만 실행이 된다.

# finally 사용 예시
# 오픈한 파일이 에러 발생 여부 상관없이 무조건 닫아야 하는 경우 
# finally에 파일 닫는 로직을 작성한다.


##################################################################


##################################################################

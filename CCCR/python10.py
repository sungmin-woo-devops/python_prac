# 딕셔너리
# 데이터 시각화 및 분석에 많이 쓰임
# 키와 값의 형태로 이루어져 있음

# 딕셔너리는 순서가 필요 없는 자료형으로 키 기반으로 값을 찾음

# 문자열, 리스트, 튜플은 시퀀스 자료형 
# = 순서 있음 = 인덱싱, 슬라이싱 가능


dic = {
    'name' : 'sungmin', 
    'phone' : '01022223333',
    'birth' : '990612'
}

print(dic)
print(type(dic))
# {'name': 'sungmin', 'phone': '01022223333', 'birth': '990612'}
# <class 'dict'


# 딕셔너리 안에 리스트 또한 값으로 사용 가능
a = {'a' : [1,2,3]}

# 딕셔너리 생성하는 다른 방법
a = dict(key='value', number=1)
print(a)
# {'key': 'value', 'number': 1}

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b' # key는2, value는 'b'
print(a)

# 함수를 키나 값으로 활용 가능
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

action = {0:add, 1:sub}
print(action[0](1, 2)) # 3
print(action[1](1, 2)) # -1

# 딕셔너리 요소 제거
dic = {
    'name' : 'sungmin', 
    'phone' : '01022223333',
    'birth' : '990612'
}
del dic['birth']
print(dic) # {'name': 'sungmin', 'phone': '01022223333'}

# 값 얻기
dic = {
    'name' : 'sungmin', 
    'phone' : '01022223333',
    'birth' : '990612'
}
print(dic['name']) # sungmin

# 딕셔너리 관련 함수들
# 키 리스트 만들기

# 리스트 형태로 딕셔너리의 key 출력
# dict_keys(['name', 'phone', 'birth'])
print(dic.keys()) 

# 리스트 형태로 딕셔너리 value 출력
# dict_values(['sungmin', '01022223333', '990612'])
print(dic.values())

# 키와 값을 쌍으로 가져오기(묶기)
# item 튜플로 이루어진 리스트 반환
# dict_items([('name', 'sungmin'), ('phone', '01022223333'), ('birth', '990612')])
print(dic.items())

# 키와 값 쌍 모두 지우기
dic.clear()
print(dic)

# 키로 값 얻기
dic = {
    'name' : 'sungmin', 
    'phone' : '01022223333',
    'birth' : '990612'
}
print(dic.get('name')) 

# 딕셔너리로 직접 찾는 것과 get() 함수로 찾는 방법의 차이점
# 없는 걸 검색
# 직접 찾는 것: dic['name']

# print(dic['nokey']) # KeyError: 'name' - 에러 발생 - 코드 멈춰
print(dic.get('nokey')) # None - 에러 발생 X - 코드 진행해


# 키가 딕셔너리 안에 있는지 확인(KEY in DICT)
print('name' in dic) # True
print('nokey' in dic) # False
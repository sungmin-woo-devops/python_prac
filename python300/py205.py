# 함수가 정의되기 전에 호출되어 에러가 발생한다.
hello()
def hello():
    print("Hi")
'''
Traceback (most recent call last):
  File "/home/w/Workspace/python/python300/py205.py", line 2, in <module>
    hello()
NameError: name 'hello' is not defined. Did you mean: 'help'?
'''

'''
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment


튜플은 불변객체로 값 삭제 혹은 수정을 할 수 없다.
(해설)tuple은 원소(element)의 값을 변경할 수 없습니다.
'''


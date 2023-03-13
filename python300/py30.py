string = "abcd"
string.replace('b','B')
print(string) 
# aBcd (X), abcd (O)
"""
abcd가 그대로 출력된다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문이다.
replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
"""

# 특정 패키지를 명시하지 않고 모든 모듈을 부를 경우 에러 발생
from game.sound import *
echo.echo_test() # NameError / name 'echo' is not defined

# 패키지 내부에서 모든 모듈을 호출할 경우 __init__.py에 수정 필요
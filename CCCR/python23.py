# 패키지
# 패키지는 폴더와 파일의 묶음
# 패키지를 의미하는 __init__.py 파일이 반드시 존재해야 함

# import echo # ModuleNotFoundError

# 디렉터리 내 __init__.py 파일이 있어야 접근 가능 = 패키지임을 명시

# 패키지 import 방법 1
import game.sound.echo 
game.sound.echo.echo_test()

# 패키지 import 방법 2
from game.sound import echo
echo.echo_test()

# 패키지에서 일부만(변수, 함수) 가져오는 경우
# 특정 함수 echo_test()만 import
from game.sound.echo import echo_test
echo_test()

# sound 패키지 전체를 import하는 방법
# echo.py, wav.py 모두 불러와 사용
from game.sound import *
echo.echo_test()

########################################################################

# 추가로 읽어볼만한 자료

# 1. import * 를 지양해야 하는 이유
# https://stackoverflow.com/questions/2386714/why-is-import-bad
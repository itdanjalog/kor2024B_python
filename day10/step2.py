# 모듈
# https://github.com/itdanjalog/tj_2024A_python/blob/master/src/day07/2_%EB%AA%A8%EB%93%88.py

# day07 > 2_모듈.py
# [1] import 모듈이름
import mod1
mod1.add( 3 , 4 )  # 모듈이름.함수명( )

# [2] from 모듈이름 import 함수명 , 함수명
from mod1 import add
add( 3 , 4 ) #  함수명( )

# [3] from 모듈이름 import *
from mod1 import *
sub( 3 , 4 )

# [4]
import mod2
print( mod2.PI )  # 3.141592

a = mod2.Math()
print( a ) # <mod2.Math object at 0x00000244FE12D460>
print( a.solv( 2 ) ) # 12.566368

print( mod2.add( 3 , 4 ) )

from mod2 import Math , PI
print( PI ) # 3.141592
b = Math()
print( b )  # <mod2.Math object at 0x000001ECF358D760>

# [5] 다른 패키지의 모듈 호출
# from day06.Task6 import User
# s = User()
# print( s )  # <src.day06.Task6.User object at 0x0000023D8B06DC70>

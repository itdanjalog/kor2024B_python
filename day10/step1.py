# 상속
#https://github.com/itdanjalog/tj_2024A_python/blob/master/src/day07/1_%ED%81%B4%EB%9E%98%EC%8A%A4.py

#[4] 상속
    # 상속 : 상위클래스로부터 물려받아 클래스 연장하기 .
#(1) 하위 클래스 정의 , class 클래스명( 상위클래스명 ) :
class MoreFourCal( FourCal ) :
    # 메서드 정의
    def pow(self):
        return self.first ** self.second
    # 오버라이딩 : 상위클래스의 메서드 재정의
    def div(self): # 메서드 선언부를 동일하게 작성
        if self.second == 0 :
            return 0
        else:
            return self.first / self.second

#(2) 하위 클래스로 객체 생성
a = MoreFourCal( 4 , 2 )
print( type(a) )    # <class '__main__.MoreFourCal'>
print( a.add() )    # 6  # 상위클래스의 메소드 호출

print( a.pow() )    # 본인클래스의 메소드 호출
print( a.div() )    # 오버라이딩 된 메서도 호출

# [5] 클래스 변수
    # 객체 변수 : # 객체 마다의 사용되는 변수 # 객체변수명.변수명 # 필드 , 멤버변수 라고도 한다.
    # 클래스 변수 :  # 모든 객체가 공유 해서 사용하는 변수  # 클래스명.변수명
        # 객체변수와 클래스변수 의 이름이 같아도 식별이 가능하다.
class Family :
    lastname = "김" # 클래스변수
print( Family.lastname )    # 김
a = Family()
print( a.lastname )         # 김
b = Family()
print( b.lastname )         # 김
Family.lastname = "박"
print( f'{ a.lastname } , { b.lastname } ') # 박 , 박
'''
    - 시나리오1 : Todo(할일) List 애플레이션 개발
        - 조건1 : 할일내용 과  할일상태를 여러번 저장 한다.
        - 조건2 : 저장 , 할일전체출력 , 상태수정 , 할일삭제 기능을 선택하여 실행한다.
        - 조건3 : 출력 예시
            순번  할일내용    할일상태           딕셔너리
            1    파이썬공부    X                     key : 할일내용      value : 파이썬공부
            2    운동하기     O                클래스/객체
            3    집가기       X                    self.할일내용 = 파이썬공부
        - 조건4 : 클래스/객체 사용 가능 합니다.

    - 요구사항 의 자료/값 와 이벤트/함수
        자료 : 할일내용 , 할일상태
        행위 : 저장 , 전체출력 , 수정 , 삭제
'''

# [1] 객체 와 리스트를 이용한 메모리 설계
class Todo :
    def __init__(self , content , state ):
        self.content = content
        self.state = state
    # 메소드
    def save( self ):
        toDoList.append( self )
    # 메소드
    def info( self , num ):
        print( f'{ num } \t { self.content } \t { self.state }')

    def update(self , state ):
        self.state = state

    def delete(self ):
        toDoList.remove( self )

toDoList = [  Todo( '파이썬공부' , '미완료') , Todo( '운동하기' , '완료') ,  Todo( '집가기' , '미완료') ]
    # 각 객체 3개를 하나의 리스트에서 관리

# [2]
while True :
    choose = input('1.저장 2.전체출력 3.상태수정 4.삭제 5.종료')
    if choose == '5':
        break  # 무한루프 종료
    if choose == '1':
        content = input('할일내용:')
        state = '미완료'
        task1 = Todo( content , state )
        task1.save()
    if choose == '2':
        num = 0
        for element in toDoList :
            num += 1
            element.info( num )
    if choose == '3' :
        num = 0
        for element in toDoList :
            num += 1
            element.info( num )
        num = int( input('수정할 순번 선택 : ') )
        state = input('수정할 상태 : ')
        toDoList[num-1].update(state)
    if choose == '4' :
        num = 0
        for element in toDoList :
            num += 1
            element.info( num )
        num = int(input('삭제할 순번 선택 : '))
        toDoList[num-1].delete()














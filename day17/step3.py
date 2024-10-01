# [3] 파이썬을 이용한 큐 구조 구현 예제
# 1. 큐 를 구현하기 위한 리스트 선언
queue = [ None, None , None , None ]
# 2. 데이터들의 위치를 저장할 변수 선언
front = -1  # 나가는 인덱스의 위치 기억 변수 선언
rear = -1   # 들어오는 인덱스의 위치 기역 변수 선언
# 3. 임의 데이터를 삽입하자
rear += 1   # 한칸 증가 # 0
queue[ rear ] = '유재석'
print( queue )              # ['유재석', None, None, None]
rear += 1   # 한칸 증가 # 1
queue[ rear ] = '강호동'
print( queue )              # ['유재석', '강호동', None, None]
rear += 1   # 한칸 증가 # 2
queue[ rear ] = '서장훈'
print( queue )              # ['유재석', '강호동', '서장훈', None]

# 4. 임의 데이터를 삭제하자
front += 1
queue[ front ] = None
print( queue )
front += 1              # [None, '강호동', '서장훈', None]
queue[ front ] = None
print(queue)            # [None, None, '서장훈', None]
front += 1
queue[ front ] = None   # [None, None, None, None]
print( queue )























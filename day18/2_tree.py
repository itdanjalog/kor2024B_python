'''
    실습1
        - 편의점 에서 판매된 물건 목록을 출력 하는 이진 트리 구조 구현
        - 하나의 제품이 여러개 가 판매되었을때 중복을 제외한 판매한 제품만 출력
'''
import random

# 1. 제품 목록
dataArray = [ '바나나맛우유' , '포켓몬빵' , '삼다수' , '코카콜라' , '삼각김밥' , '칠성사이다' , '츄파춥스' ]

# 2. 난수 를 이용한 제품 판매
    # 난수를 생성 해주는 객체 : random     ,   import random
print( random )
print( random.randint )
x = random.random();             print( x )     # 0 ~ 1 사이의 실수
y = random.randint( 10 , 20 );   print( y )     # 10 ~ 20 사이의 정수
z = random.choice('동해물과백두산이'); print( z )  # 문자열 중에 하나의 문자를 난수로 추출

sellArray = [  random.choice( dataArray ) for _ in range( 10 ) ]
    # [ 데이터 for _ in range( 길이 ) ]  : 길이만큼의 데이터를 요소로 생성

print( f' 판매된 제품 목록 : { sellArray }' )

# 3. 판매된 제품목록의 이진 트리 구조 만들기
    # 3-1 node 클래스 선언
class TreeNode :
    def __init__(self):
        self.left = None # 왼쪽 자식노드
        self.data = None # 현재 노드의 데이터
        self.right = None # 오른쪽 자식노드

    # 3-3 root 노드 객체 만들기
rootNode = TreeNode()
rootNode.data = sellArray[0]    # 판매목록중에 첫번째 데이터가 root node
print( rootNode.data )

    # 3-4 반복문을 이용한 이진트리 구조 저장하기
for name in sellArray[ 1 : ]    : # 첫번째 제품을 제외한 두번째 판매 제품 부터 끝까지 반복문
    print( f' 노드생성 : { name }' , end = '\t')
    node = TreeNode()   # 새로운 노드
    node.data = name    # 새로운 노드에 판매된 제품명 대입

    current = rootNode # 비교할 현재 부모 노드의 위치 , root 부터 시작
    # 방금 생성된 node 기준의 current(부모노드) 와 비교해서 작으면 왼쪽 , 크면 오른쪽
        # 자식노드가 이미 존재하면 current를 왼쪽 , 오른쪽으로 이동후 다시 비교
    while True :
        if name < current.data : # 만약에 부모 노드 보다 작으면 왼쪽 자식노드 에 대입
            if current.left == None : # 왼쪽 자식노드가 비어있으면
                current.left = node     # 방금 생성된 노드를 대입
                break                   # 가장 가까운 반복문 ( while ) 탈출
            current = current.left    # 왼쪽 자식노드가 비어있지 않으면 왼쪽 자식 노드 으로 이동
        elif name > current.data : # 만약에 부모 노드 보다 크면 오른쪽 자식노드 에 대입
            if current.right == None : # 오른쪽 자식노드가 비어있으면
                current.right = node    # 방금 생성된 노드를 대입
                break
            current = current.right # 오른쪽 자식노드가 비어있지 않으면 오른쪽 자식 노드 으로 이동
        else : # 만약에 부모 노드 와 같으면 저장 안함, 중복 제거
            break

    # 3-5 전위 순회 함수 : root -> left -> right
def preorder( node ) :
    if node == None : return   # 만약에 node가 비어있으면 함수 종료
    print( node.data , end ='\t') # end='\t' : 출력시 줄바꿈 대신 \t .
    # 재귀 함수
    preorder( node.left )   # 왼쪽노드 확인
    preorder( node.right )  # 오른쪽노드 확인

    # 3-5 중위 순회 함수 :  left -> root -> right
def inorder( node ) :
    if node == None : return
    inorder(node.left)  # 왼쪽노드 확인
    print( node.data , end ='\t')
    inorder( node.right )  # 오른쪽노드 확인

    # 3-6 후위 순회 함수 : left -> right -> root
def postorder( node ) :
    if node == None : return
    postorder(node.left)  # 왼쪽노드 확인
    postorder( node.right )  # 오른쪽노드 확인
    print( node.data , end ='\t')

preorder( rootNode )        # 전위 순회
print()
inorder( rootNode )         # 중위 순회 : 오름차순 ( 가나다 순 )
print()
postorder( rootNode )       # 후위 순회
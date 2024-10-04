# 파이썬에서 이진트리를 구현하는 방법
# Node 클래스 를 이용한 구현
# [1] Node 클래스 정의하기
    # 클래스란? 객체를 생성하기 위한 설계도
class TreeNode :
    # 생성자 란? 객체를 생성할때 초기화하는 함수
    def __init__(self):
        # 속성 이란? 객체가 가지는 고유값를 저장하는 필드/변수
        self.left = None # 객체 생성시 속성의 초기값
        # None 이란 ? 데이터 가 없다는 뜻
        self.data = None
        self.right = None
# [2] None 객체 만들기
rootNode = TreeNode( ) # Node 객체 생성
rootNode.data = "유재석" # rootNode 객체 data 속성에 '유재석' 대입
# [3] Node 객체 만들기
node1 = TreeNode()
node1.data = '강호동' # node1 객체 data 속성에 '강호동' 대입
rootNode.left = node1 # rootNode 객체 left 속성에 node1 대입 했다.
#
node2 = TreeNode()
node2.data = '신동엽'
rootNode.right = node2 # rootNode 객체 right 속성에 node2 대입 했다.
#
node3 = TreeNode()
node3.data = '서장훈'
# rootNode 더이상 자식노드를 가질수 없다( left,right 포화 )
node1.left = node3 # node1 객체 left 속성에 node3 대입 했다.
#
node4 = TreeNode()
node4.data = '김희철'
node2.right = node4
#
node5 = TreeNode()
node5.data = '우원재'
node3.left = node5

























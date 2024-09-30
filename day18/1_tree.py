'''
    자료구조 : 자료 들을 저장 하는 방법
        1.stack : 선형 자료구조 , 후입선출
        2.queue : 선형 자료구조 , 선입선출
        3.tree : 비선형 자료구조

    선형 자료구조 : 자료가 뒤로 하나씩 존재 하는 구조
        - 리스트 , 스택 , 큐 등등
        5 -> 6 -> 2 -> 1 -> 7

    비선형 자료구조 : 자료가 뒤로 여러개 존재 하는 구조
        - 트리 , 그래프 등등
            ->  3  -> 3 , 5
        5
            ->  4  -> 6 , 2

    [1] 이진 트리
        - 데이터를 저장하는 비선형 자료구조
        - 각 노드가 최대 2개의 자식 노드를 가질수 있는 트리 구조
        - 왼쪽 자식노드에는 부모 보다 작은 데이터 , 오른쪽 자식노드에는 부모 보다 큰 데이터
        - 사용처 : 데이터 검색, 정렬 , 파일 시스템 등등
        - 장점
            1. 계층형 구조 표현  2.재귀구조 표현 , 3.효율적인 메모리관리(저장할때부터 데이터정렬)
        - 용어
            1. 노드 : 데이터가 들어가는 공간
            2. 부모노드 : 특정 노드의 바로 위 노드
            3. 자식노드 : 특정 노드의 바로 아래에 있는 노드들 , 이진트리는 최대 2개 갖는다.
            4. 루트노드 : 트리의 맨위에 있는 노드로 , 루트노드는 트리의 시작하는 경로를 뜻한다.
            5. 깊이 : 루트노드에서 특정 노드까지의 경로의 길이
            6. 높이 : 트리의 최대 깊이 , 가장 깊은 노드의 길이

        - 순회 : 이진트리 에서 node를 읽는 순서 , root를 읽는 순서에 따라 종류 3가지
            전위 순회 : root -> left -> right
            중위 순회 : left -> root -> right , 오름차순
            후위 순회 : left -> right -> root

        - 구조 확인
            예시1 :  [ 23 , 7 , 9 , 12 , 52 , 42 , 30 ]
            이진 트리 형식 으로 표현 하시오.
                            [23]
              [7]                           [52]
                  [9]                   [42]
                      [12]         [30]

            예시2 :  [ 32 , 15 , 10 , 18 , 33 , 42 , 21 ]
            - ppt 참고
'''
# 파이썬에서 이진트리 만드는 방법 , 클래스와 객체
# [1] Node 클래스 정의하기
class TreeNode : # class 정의하기
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# [2] Node 객체 만들기
rootNode = TreeNode()   # Node 객체 생성
rootNode.data = "유재석"   # 객체내 'data' 속성에 "유재석" 대입

node1 = TreeNode()      # Node 객체 생성
node1.data = "강호동"   # 객체내ㅑ 'data' 속성에 '강호동' 대입
rootNode.left = node1

node2 = TreeNode()
node2.data = "신동엽"
rootNode.right = node2

node3 = TreeNode()
node3.data = '서장훈'
node1.left = node3

node4  = TreeNode()
node4.data = '김희철'
node2.right = node4

node5 = TreeNode()
node5.data = "우원재"
node3.left = node4



print( rootNode.left , rootNode.data , rootNode.left  , rootNode.left.data )
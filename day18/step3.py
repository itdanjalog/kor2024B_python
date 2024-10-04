# 파이썬에서 이진트리를 구현하는 방법
# 1. Node 클래스
class TreeNode :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
# 5. 이진트리 삽입 함수 만들기
def insert( root , value ) :
    # 만약에 root 가 None 이면 # 즉 첫번째 반복 이면 # 즉 root노드 이면
    if root is None :
        node = TreeNode()
        node.data = value
        return node
    # 두번째 반복 이면 # 즉 root 노드가 아니면
    if value < root.data : # 부모 노드보다 값이 작으면
        root.left = insert( root.left , value ) # 왼쪽에 삽입  # 재귀함수
    elif value > root.data: # 부모 노드보다 값이 크면
        root.right = insert( root.right , value ) # 오른쪽에 삽입  # 재귀함수
        # 부모의 오른쪽 = insert( 부모의 오른쪽 , 대입값 )
    return root
# 2. 샘플 데이터 # 샘플 데이터를 하나씩 이진트리로 표현
list = [ 3 , 5 , 2 , 1 , 9 ]
# 3. 루트 노드 생성
rootNode = None
# 4. 샘플 데이터를 반복문 하기
for value in list : # 5번 반복
    # 정의한 insert 함수를 호출
    rootNode = insert( rootNode , value )

# 6. root 노드에 중위 순회 : 중위 순회란. left -> root -> right 순으로 전체 노드를 순회하는 방법 # 정렬
def inorder( node ) :
    if node == None : return
    # 중위 : 왼쪽 -> 부모 -> 오른쪽
    inorder( node.left ) # 왼쪽 노드 # 재귀 함수
    print( node.data , end = '\t' ) # 부모 노드
    inorder( node.right ) # 오른쪽 노드 # 재귀 함수
# 7. 이진 트리 를 중위 순회 하기.
inorder( rootNode ) #  1	2	3	5	9	 # 중위순회란 작은 값부터 끝값을 순회 방식 # 즉] 오름차순

# 순서도 / 알고리즘
'''
                                                     if root is None : 
    [1번째 반복문] rootNode = None , value = 3 일때         true                 return TreeNode[ left = None , data = 3 , right = None ]
    [1번째 반복문 종료 ] rootNode = TreeNode[ left = None , data = 3 , right = None ]
    
    [2번째 반복문] rootNode = 객체(data=3)  , value = 5 일때    false              5 > 3 오른쪽 이동 
        [ 재귀 ] root.right( None ) , value = 5 일때          true                return TreeNode[ left = None , data = 5 , right = None ]
        [ 재귀 끝 ] 
    [2번째 반복문 종료 ] return TreeNode[ left = None , data = 3 , right = TreeNode[ left = None , data = 5 , right = None ] ]
    
    [3번째 반복문] rootNode = 객체(data=3) , value = 2 일때     false              2 <  3  왼쪽 이동 
        [ 재귀 ] root.left( None ) , value = 2 일때           true              return TreeNode[ left = None , data = 2 , right = None ]
        [ 재귀 끝 ]
    [3번째 반복문 종료 ] 
        return TreeNode[ 
            left = TreeNode[ left = None , data = 2 , right = None ] , 
            data = 3 , 
            right = TreeNode[ left = None , data = 5 , right = None ] ]
    
    [4번째 반복문] rootNode = 객체(data=3 ) , value = 1 일때     false              1 < 3   왼쪽 이동 
        [ 재귀] root.left ( data=2 ) , value = 1 일때          false              1 < 2   왼쪽 이동 
            [재귀] root.left( None ) , value = 1 일때          true             return TreeNode[ left = None , data = 1 , right = None ]
                [ 재귀 끝 ] root.left = TreeNode[ left = None , data = 1 , right = None ]
                    [ 재귀 끝 ]
    [4번째 반복문 종료 ]
        return TreeNode[ 
            left = TreeNode[ left = TreeNode[ left = None , data = 1 , right = None ]  , data = 2 , right = None ] , 
            data = 3 , 
            right = TreeNode[ left = None , data = 5 , right = None ] ]
    
    예측 [ 5번째 반복문 ]
        return TreeNode[ 
            left = TreeNode[ left = TreeNode[ left = None , data = 1 , right = None ]  , data = 2 , right = None ] , 
            data = 3 , 
            right = TreeNode[ left = None , data = 5 , right = TreeNode[ left = None , data = 9 , right = None ] ] ]
'''

































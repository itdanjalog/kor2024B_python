# 이진 검색 트리의 노드 클래스 정의
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 검색 트리 클래스 정의
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # 노드를 트리에 삽입하는 함수
    def insert(self, value):
        # 새로운 노드를 생성
        new_node = TreeNode(value)
        # 트리가 비어있으면 루트로 설정
        if self.root is None:
            self.root = new_node
        else:
            # 트리 내에 값을 삽입하는 내부 함수
            self._insert_recursive(self.root, new_node)
    
    def _insert_recursive(self, current, new_node):
        # 중복 허용하여 같은 값을 왼쪽에 삽입
        if new_node.value <= current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    # 중복 허용 이진 트리 검색 함수
    def search_duplicates(self, value):
        pos_list = []
        self._search_recursive(self.root, value, pos_list, 0)
        return pos_list
    
    # 검색을 재귀적으로 처리하는 내부 함수
    def _search_recursive(self, current, value, pos_list, level):
        if current is not None:
            # 왼쪽 서브트리 탐색
            self._search_recursive(current.left, value, pos_list, level + 1)
            # 현재 노드의 값이 찾는 값과 같으면 위치(레벨) 기록
            if current.value == value:
                pos_list.append(level)
            # 오른쪽 서브트리 탐색
            self._search_recursive(current.right, value, pos_list, level + 1)

# 코드 실행

# 이진 검색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입 (샘플 데이터 목록)
data_list = [188, 162, 168, 120, 50, 150, 177, 105, 150] # 150 중복

# 데이터 삽입
for data in data_list:
    bst.insert(data)

# 검색할 데이터 입력
find_value = int(input('검색할 데이터: '))

# 중복 검색 함수 호출
pos_list = bst.search_duplicates(find_value)

# 검색 결과 출력
if len(pos_list) == 0:
    print(find_value, '의 검색 결과가 존재하지 않습니다.')
else:
    print(find_value, '의 검색 결과는', pos_list, '레벨에 존재합니다.')

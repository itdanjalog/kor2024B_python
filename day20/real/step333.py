class HashTable:
    def __init__(self, size):
        self.size = size  # 해시 테이블 크기
        self.table = [[] for _ in range(size)]  # 해시 테이블 초기화

    def hash_function(self, key):
        # 해시 함수 (단순 나머지 연산 사용)
        return key % self.size

    def insert(self, value):
        index = self.hash_function(value)  # 해시 값 계산
        print( index )
        self.table[index].append(value)  # 해당 인덱스에 값 추가

    def search_duplicates(self, value):
        index = self.hash_function(value)  # 해시 값 계산
        # 해당 인덱스에서 중복된 값 검색
        pos_list = [i for i, v in enumerate(self.table[index]) if v == value]
        return pos_list

# 코드 실행

# 해시 테이블 크기 설정
hash_table = HashTable(size=10)

# 데이터 삽입 (샘플 데이터 목록)
data_list = [188, 162, 168, 120, 50, 150, 177, 105, 150]  # 150 중복

# 데이터 삽입
for data in data_list:
    hash_table.insert(data)

print( hash_table.table )

# 검색할 데이터 입력
find_value = int(input('검색할 데이터: '))

# 중복 검색 함수 호출
pos_list = hash_table.search_duplicates(find_value)

# 검색 결과 출력
if len(pos_list) == 0:
    print(find_value, '의 검색 결과가 존재하지 않습니다.')
else:
    print(find_value, '의 검색 결과는', pos_list, '인덱스에 존재합니다.')

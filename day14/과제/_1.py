import matplotlib.pyplot as plt

# 주어진 데이터
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 선 그래프 그리기
plt.plot(x, y, marker='o')

# 그래프 제목 및 축 레이블 설정
plt.title("line chart")
plt.xlabel("X value")
plt.ylabel("Y value")

# 그리드 표시
plt.grid()

# 그래프 보여주기
plt.show()
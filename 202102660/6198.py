# 자료구조
# 다시 풀기
import sys
from collections import deque

n = int(sys.stdin.readline())
building = [int(sys.stdin.readline()) for _ in range(n)]
st = deque()
st.append(building[0])
sum = 0

for i in range(1, n):
    while st and st[-1] <= building[i]:
        # 이전 빌딩이 지금 빌딩보다 작으면 빼내야함
        st.pop()
    st.append(building[i])
    sum += len(st)-1

print(sum)
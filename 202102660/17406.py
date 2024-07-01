# 크기가 N×M 크기인 배열 A가 있을때, 배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다.
# 첫째 줄에 배열 A의 크기 N, M, 회전 연산의 개수 K가 주어진다.
#
# 둘째 줄부터 N개의 줄에 배열 A에 들어있는 수 A[i][j]가 주어지고, 다음 K개의 줄에 회전 연산의 정보 r, c, s가 주어진다.

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 회전 연산시 r, c는 -1 씩 해줘야함
commands = [tuple(map(int, input().split())) for _ in range(K)]
comm_dict = dict()
visited = dict()
min_val = 10000000
# commands의 순열 구하기
# 각 커맨드별로 갯수 딕셔너리 만들기
for comm in commands:
    if comm not in comm_dict.keys():
        comm_dict[comm] = 0
        visited[comm] = 0
    comm_dict[comm] += 1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
def rotate(command, A):
    new_A = [a[:] for a in A]
    (r, c, s) = command
    r -= 1
    c -= 1
    for ss in range(s, 0, -1): # ss가 0 되면 멈춰야함. 안움직이니까
        n = 0
        x = r-ss
        y = c-ss
        while n<2*ss*4:
            d = n // (2 * ss)
            new_A[x + dx[d]][y + dy[d]] = A[x][y]
            x, y = x + dx[d], y+dy[d]
            n += 1
    return new_A



def get_val(A):
    return min(map(sum, A))

# 딕셔너리의 키로 만듦
def get_permute(n, A):
    global min_val, K
    # 리스트 원소 수가 K가 되면
    if n == K:
        # 리스트 복사해서
        # copy_A = [a[:] for a in A]
        # 복사된 리스트 명령대로 회전 후 배열 값 구하기
        # copy_A = rotate(ncomm, A)
        # 현재 최소 값 비교 업데이트
        min_val = min(min_val, get_val(A))
        # 리턴
        return
    for key in comm_dict.keys():
        # 해당 원소의 visited 딕셔너리 개수와 사용가능 딕셔너리 개수와 비교해서 더 작으면 ㄱㄱ
        if visited[key] < comm_dict[key]:
            # visited += 1 하고
            visited[key] += 1
            # 리스트에 넣어서 재귀호출
            new_A = [a[:] for a in A]
            new_A = rotate(key, new_A)
            get_permute(n+1, new_A)
            # visited -= 1
            visited[key] -= 1
    return

get_permute(0, A)
print(min_val)
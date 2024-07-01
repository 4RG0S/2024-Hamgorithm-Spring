'''
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
'''
import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

'''
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
'''

# 각 번호대로 0번부터 
# 팀1에 속하는경우,
    # 각 팀에 넣을때마다 팀별 능력치 계산
# 팀2에 속하는 경우
# 하다가 각 팀에 사람이 다 차면 능력치 차이 계산
min_diff = 10**10

def calc_score(team, score, idx, i):
    # idx: 새로 넣을 사람
    # i: 넣을 팀
    # score[i] 업데이트
    # team[i]의 p에 대해 S[p][idx], S[idx][p]를 score[i]에 더하기
    new_score = score[:]
    for p in team[i]:
        new_score[i] += (S[p][idx] + S[idx][p])
    return new_score

def divide(idx, score, team):
    global N, min_diff
    # idx: 넣은 사람 번호
    # score 팀별 능력치합 리스트
    # team[0] 0팀 사람 번호 리스트, [1] 1팀 사람 번호 리스트
    
    if idx == N-1:
        diff = abs(score[0]-score[1])
        min_diff = min(min_diff, diff)
        return
    
    for i in range(2):
        # 팀에 인원이 다 차지 않은 경우
        if len(team[i]) < N//2:
            new_score = calc_score(team, score, idx+1, i)
            new_team = [t[:] for t in team]
            new_team[i].append(idx+1) # 다음사람 넣기
            divide(idx+1, new_score, new_team)

divide(-1, [0, 0], [[],[]])
print(min_diff)
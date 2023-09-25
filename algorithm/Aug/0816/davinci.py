'''다빈치 민코드 게임은 1 : 1 로 대결하는 보드게임입니다.
이 게임에는 N개의 패가 등장합니다.
각 패에는 -9 ~ 9 사이의 수가 적혀있습니다.

여러개의 패 중, 상대에게 M개의 패를 전달해 주어야 합니다.
M개의 패에 적혀있는 수들의 곱이 최소값이 되면, 나의 승리가 됩니다.

상대의 곱이 최소패가 되도록 하려면,
어떤 패들을 주어야하는지 오름차순으로 순서대로 출력해 주세요.

입력
패의 개수 N과 뽑아야 하는 개수 M 이 입력 됩니다. (3 <= M < N <= 40)
그 다음 줄에는 패에 적혀있는 수들이 입력 됩니다.

출력
M개의 곱이 최소값이 되기 위해 선택해야 하는 패의 종류를
오름차순 순서대로 출력합니다.
'''
import copy
N, M = map(int, input().split())
hands = list(map(int, input().split()))
path = [] # 선택된 패들의 값을 저장할 리스트입니다.
used = [0] * N
Min = 20e8
result = []

def DFS(level, mul):
    global Min, path, result
    if level == M:  # 패를 모두 선택했다면
        if mul < Min: #현재 곱한 값이 최소값보다 작으면 최소값을 초기화
            Min = mul
            result = path[:]
        return

    for i in range(N):
        if used[i] == 1:
            continue            # 이미 사용된 패는 건너뜀
        path.append(hands[i])   # 패를 선택하고 path에 추가
        used[i] = 1
        DFS(level + 1, mul * hands[i])
        used[i] = 0     # 복구 (백트래킹)
        path.pop()

DFS(0, 1) # 초기 레벨은 0, 초기 곱은 1
result.sort()
print(*result)
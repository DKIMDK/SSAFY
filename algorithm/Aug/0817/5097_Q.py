from collections import deque
d = deque()
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cQ = list(map(int, input().split()))
    # d.extend(cQ)
    # d.rotate(-M)
    # print(f'#{tc} {d[0]}')
    # d.clear()
    for i in range(M):
        cQ.append(cQ.pop(0))
    ans = cQ[0]
    print(f'#{tc} {ans}')
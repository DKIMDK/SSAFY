from collections import deque

def bfs(g):
    q = deque()
    check = [False for _ in range(n)]
    q.append(g[0])
    check[g[0]] = True

    cnt, answer = 1, 0
    while q:
        temp = q.popleft()
        answer += people[temp]
        for i in board[temp]:
            # i는 인접한 값
            # 그 값이 g 배열 안에 있고 방문한 적 없으면 계속 진행
            if i in g and not check[i]:
                check[i] = True
                cnt += 1
                q.append(i)

        if cnt == len(g):
            return answer
        else:
            return False

def dfs(cnt, x, end):
    global min_value

    # 원하는 구역의 개수만큼 도달했을 때
    if cnt == end:
        g1, g2 = deque(), deque()
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        # bfs로 g1 deque 안의 값이 인접한 값인지 확인
        ans1 = bfs(g1)
        # 아니라면 바로 함수 종료
        if not ans1:
            return
        ans2 = bfs(g2)
        if not ans2:
            return

        # 둘 다 인접한지 확인이 되었다면 최소값 확인
        min_value = min(min_value, abs(ans1 - ans2))
        return

    # 아직 end 개수에 도달하지 못했을 때는
    # for 문을 통해 그 다음구역부터 새로운 구를 만들어준다.
    for i in range(x, n):
        # 방문을 했다면 무시
        if visited[i]:
            continue
        # 하지않았다면
        visited[i] = True
        dfs(cnt + 1, i, end)

        # back tracking
        visited[i] = False

T = int(input())
for tc in range(1, T+1):



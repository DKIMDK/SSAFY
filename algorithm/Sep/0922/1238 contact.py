'''
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.

[제약 사항]
연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하이다.
단, 예시에서 5번이 존재하지 않듯이 중간 중간에 비어있는 번호가 있을 수 있다. >> 인접리스트 사용
한 명의 사람이 다수의 사람에게 연락이 가능한 경우 항상 다자 간 통화를 통해 동시에 전달한다.
연락이 퍼지는 속도는 항상 일정하다 (전화를 받은 사람이 다음사람에게 전화를 거는 속도는 동일).
비상연락망 정보는 사전에 공유되며 한 번 연락을 받은 사람에게 다시 연락을 하는 일은 없다.
예시에서의 3, 6, 11, 22번과 같이 연락을 받을 수 없는 사람도 존재할 수 있다.

[입력]
10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 입력 받는 데이터의 길이와 시작점이 주어진다.
그 다음 줄에 입력받는 데이터는 {from, to, from, to, …} 의 순서로 해석된다
그런데 순서에는 상관이 없으므로 다음과 같이 주어진 인풋도 동일한 비상연락망을 나타낸다

다음과 같이 동일한 {from, to}쌍이 여러 번 반복되는 경우도 있으며,
한 번 기록된 경우와 여러 번 기록된 경우의 차이는 없다.
{1, 17, 1, 17, 1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 11, 6, 4, 2}

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

'''
def bfs(s):
    q = [s]
    visited = [0] * 101
    # 시작점은 방문 처리
    visited[s] = 1

    # 최대 숫자와 최대 깊이를 저장
    max_number = s
    max_depth = 1
    while q:
        now = q.pop(0)

        # 갈 수 있는 지점
        for next in graph[now]:
            if visited[next]:
                continue
            # 기존 방문보다 한 번 더 갔다. -> visited에 순서를 저장
            visited[next] = visited[now] + 1

            # 한 단계 깊은 곳으로 가거나 깊이는 같은데 숫자가 더 크다면
            # max 값을 초기화
            if max_depth < visited[next] or (max_depth == visited[next] and max_number < next):
                max_depth = visited[next]
                max_number = next
            q.append(next)
    return max_number

for tc in range(1, 10 + 1):
    n, start = map(int, input().split())
    # 임시로 전체 입력을 받음
    input_graph = list(map(int, input().split()))
    # 실제 사용할 인접 리스트 -> input_graph를 사용해서 만든다
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = input_graph[i]
        t = input_graph[i + 1]
        graph[f].append(t)

    r = bfs(start)

    print(f'#{tc} {r}')

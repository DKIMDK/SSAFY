'''
민코씨는 크리스마스를 맞아 크리스마스트리에 장식을 걸었습니다.

장식에는 불빛이 들어오는데 불빛이 들어오는 패턴이 있습니다.

임의의 특정 한 장식에 대해서 다음 3가지 패턴 중 하나로 동작합니다.

현재 특정 한 장식을 A이라고 할 때, 각 패턴은 아래의 규칙대로 켜집니다.

1번 패턴
좌 - 중 - 우
2번 패턴
중 - 좌 - 우
3번 패턴
좌 - 우 - 중

입력된 크리스마스 트리에 대해,
각 패턴으로 실행하였을 때 각 장식에 불이 켜지는 순서대로 장식 번호를 출력해주세요.

[제한사항]

장식의 개수 N 은 1이상 1000 이하입니다.
장식의 번호는 1부터 N 까지 정수이며 크리스마스 트리 꼭대기에는 항상 1번 장식이 있습니다.
입력
첫 번째 줄에는 트리 장식의 개수  N 이 주어집니다. ( 1 <= N <= 1000)

다음 줄부터 N개의 줄에 걸쳐 장식의 번호와 
해당 장식의 왼쪽 장식 번호, 오른쪽 장식 번호가 공백으로 구분되어 차례로 입력됩니다.
만약 장식이 없다면 장식 번호 대신 -1이 입력됩니다.
 

출력
첫 번째 줄에 1번 패턴이 켜지는 순서를 공백으로 구분하여 출력합니다.
두 번째 줄에 2번 패턴이 켜지는 순서를 공백으로 구분하여 출력합니다.
세 번째 줄에 3번 패턴이 켜지는 순서를 공백으로 구분하여 출력합니다.

'''
N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N+1)
stack = [1]
result = []

def dfs1(now):
    while len(stack) > 0:        
        left = tree[now - 1][1]
        right = tree[now - 1][2]
        if not visited[left] and left != -1:
            visited[left] = 1
            stack.append(left)
            now = left
        elif not visited[right] and right != -1:
            visited[right] = 1
            stack.append(right)
            now = right
        else:
            result.append(stack.pop())
            if len(stack) > 0:
                now = stack.pop()
                result.append(now)
            else:
                break





def dfs3(now):
    while len(stack) > 0:        
        left = tree[now - 1][1]
        right = tree[now - 1][2]
        if not visited[left] and left != -1:
            visited[left] = 1
            stack.append(left)
            now = left
        elif not visited[right] and right != -1:
            visited[right] = 1
            stack.append(right)
            now = right
        else:
            result.append(stack.pop())
            if len(stack) > 0:
                now = stack[-1]
            else:
                break


dfs1(1)
print(*result)
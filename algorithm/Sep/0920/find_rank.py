n, m, target  = map(int, input().split())

upv = [[] for _ in range(n + 1)]    # 어떤 학생이 다른 학생보다 잘했는지
downv = [[] for _ in range(n + 1)]  # 못했는지

# up : target보다 못한 학생 수, down: target보다 잘한 학생 수
up = 1
down = 1

upused = [False] * (n + 1)
downused = [False] * (n + 1)

# target보다 못한 학생
def updfs(node):
    global up
    for next_node in upv[node]:
        if not upused[next_node]:
            up += 1
            upused[next_node] = True  # 방문 표시
            updfs(next_node)

def downdfs(node):
    global down
    for next_node in downv[node]:
        if not downused[next_node]:
            down += 1
            downused[next_node] = True  # 방문 표시
            downdfs(next_node)

for _ in range(m):
    a, b = map(int, input().split())
    upv[b].append(a)
    downv[a].append(b)

updfs(target)
downdfs(target)

print(up)
print(n - down + 1)
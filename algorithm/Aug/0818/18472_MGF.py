def D(A):
    A *= 2
    return A % 10000, 'D'
def S(A):
    A -= 1
    return A if A >= 0 else 9999, 'S'

def L(A):
    a = []
    for i in str(A):
      a.append(i)
    a.append(a.pop(0))
    k = ''.join(a)
    return int(k), 'L'

def R(A):
    a = []
    for i in str(A):
      a.append(i)
    a.insert(0, a.pop())
    k = ''.join(a)
    return int(k), 'R'

def solution(start, end):
    queue = [(start, [])]
    visited = {start}
    while queue:
        now, trial = queue.pop()
        if now == end:
            return trial
        possible = [D(start), S(start), L(start), R(start)]
        for next_n, next_s in possible:
            if next_n not in visited:
                visited.add(next_n)
                queue.append((next_s, ))



N = int(input())
for _ in range(N):
    A, B = map(int, input().split())



def solution(start, end):
    maximum = 100000
    queue = [(start, 0)]
    visited = {start}
    while queue :
        now, cnt = queue.pop(0)
        calc = [now + 1, now - 1, now * 2, now // 2]
        for next in calc:
            if next == end:
                return cnt + 1
            if 0 <= next <= maximum:
                if next not in visited:
                    visited.add(next)
                    queue.append((next, cnt + 1))
    return -1

S = int(input())
D = int(input())

print(solution(S, D))
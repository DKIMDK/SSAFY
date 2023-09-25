def solution(n, k):
    if n//10 == n:
        return k
    else:
        return solution(n//10, k + n % 10)

print(solution(12345, 0))
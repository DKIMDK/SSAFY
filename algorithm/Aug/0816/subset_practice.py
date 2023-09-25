def f(i, N, s, t): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합), t : 찾으려는 합
    global cnt
    cnt += 1
    if s == t:              # 합이 목표에 도달했으면
        print(bit)
        return
    elif i == N:
        if s == t:
            print(bit)
        return
    elif s > t:
        return
    else:
        bit[i] = 1          # 부분집합에 A[i] 포함
        f(i + 1, N, s+A[i], t)
        bit[i] = 0          # 부분집합에 A[i] 미포함
        f(i+1, N, s, t)
        return
# 1부터 10까지 원소인 집합 A, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N + 1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 1)
print(cnt)
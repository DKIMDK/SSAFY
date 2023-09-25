def f(i, N):
    if i == N:
        return
    else:
        f(i+1, N)
N = 5
A = [1, 2, 3, 4, 5]

f(0, N)

# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, arr):
    if i == N:
        return
    else:
        f(i+1, N, key, arr)
N = 5
A = [1, 2, 3, 4, 5]
key = 3
f(0, N, key, arr)
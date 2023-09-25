A = [1, 2, 3]
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

f(0, 3)